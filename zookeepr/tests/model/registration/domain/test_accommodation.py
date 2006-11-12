from sqlalchemy import default_metadata

from zookeepr.tests.model import *

class TestAccommodationLocationModel(ModelTest):
    """Test the AccommodationLocation crud object, that maps straight on
    top of the accommodation_location table.
    """
    domain = model.registration.AccommodationLocation
    samples = [dict(name="nam1",
                    beds=1,
                    ),
               dict(name="name2",
                    beds=2,
                    )
               ]


class TestAccommodationOptionModel(ModelTest):
    """Test the AccommodationOption crud object, that maps straight
    on top of the accommopation_option table.
    """
    domain = model.registration.AccommodationOption
    samples = [dict(name="opt1",
                    cost_per_night=1,
                    ),
               dict(name="opt2",
                    cost_per_night=2,
                    )
               ]

    def setUp(self):
        super(TestAccommodationOptionModel, self).setUp()
        
        self.location = model.registration.AccommodationLocation(name='foo', beds=1)
        objectstore.save(self.location)
        objectstore.flush()
        self.lid = self.location.id
        
    def additional(self, ao):
        """Create location objects for the samples before they're saved.
        """
        ao.location = self.location
        return ao

    def tearDown(self):
        self.location = Query(model.registration.AccommodationLocation).get_by(id=self.lid)
        objectstore.delete(self.location)
        objectstore.flush()

        super(TestAccommodationOptionModel, self).tearDown()


class TestAccommodationModel(ModelTest):

    def test_accommodation_available(self):

        # engine echo on
        
        default_metadata.engine.echo = True
        al = model.registration.AccommodationLocation(name='a', beds=1)
        objectstore.save(al)
        objectstore.flush()
        ao = model.registration.AccommodationOption(name='', cost_per_night=1.00)
        ao.location = al
        objectstore.save(ao)
        objectstore.flush()

        print "accommodations:", Query(model.registration.Accommodation).select()

        a = Query(model.registration.Accommodation).get_by(id=1)
        self.failIfEqual(None, a)

        print "registrations using this accommodation:", a.registrations

        self.assertEqual([], a.registrations)

        self.assertEqual(1, a.get_available_beds())

        # register something, use up the bed
        r = model.registration.Registration()
        r.accommodation = a

        objectstore.save(r)
        objectstore.flush()

        print "registrations using this accommodation:", a.registrations
        self.failIfEqual([], a.registrations)
        self.assertEqual(r, a.registrations[0])

        print a.get_available_beds()
        self.assertEqual(0, a.get_available_beds())

        # add a second accommodation option
        model.registration.tables.accommodation_option.insert().execute(
            dict(id=2,
                 accommodation_location_id=1,
                 name='x',
                 cost_per_night=2.0
                 )
            )

        a1 = Query(model.registration.Accommodation).get_by(id=2)
        
        print "a beds available:", a.get_available_beds()
        print "a1 beds available:", a1.get_available_beds()

        # both options should have no beds because the first registration filled them all
        self.assertEqual(0, a1.get_available_beds(), "accommodation options should both have no beds available")

        objectstore.delete(r)
        model.registration.tables.accommodation_option.delete().execute(id=2)
        objectstore.delete(a)
        objectstore.flush()
