# File for holding configuration relative to the current LCA
# This could be dberised sometimes
from datetime import datetime


lca_info = {
  'paymentgateway_userid' : '',
  'paymentgateway_secretkey' : '',

# Contact email for the committee
  'contact_email' : 'contact@lca2011.linux.org.au',
# All email sent by ZK will Bcc here:
  'bcc_email' : 'archive@lca2011.linux.org.au',
  'webmaster_email': 'webmaster@lca2011.linux.org.au',

# Event information
  'event_parent_organisation' : 'Linux Australia',
  'event_parent_url' : 'http://www.linux.org.au/',
  'event_name' : 'linux.conf.au 2011',
  'event_shortname' : 'lca2011',
  'event_url' : 'http://lca2011.linux.org.au',
  'event_permalink' : 'http://lca2011.linux.org.au',
  'event_hashtag' : '#LCA2011',
  'event_tax_number' : 'ABN 56 987 117 479',
  'event_postal_address' : 'PO BOX 2010 Keperra, Queensland, 4054',
  'event_fax_number' : '',
  'event_phone_number': '+61 7 3103 7998',
  'event_byline': 'linux.conf.au 2011 | 24 - 29 Jan | Follow the Flow',
  'event_pricing_disclaimer': 'All prices are in Australian dollars and include 10% GST.',
  'media_license_name' : 'Creative Commons Attribution-Share Alike License',
  'media_license_url'  : 'http://creativecommons.org/licenses/by-sa/3.0/',
  #'sales_tax_multiplier' : 0.125,
  'sales_tax_divisor'    : 9,

  'invoice_message' : 'To qualify for the earlybird discount you must have registered and paid by the 30th of October (unless earlybird tickets sell out earlier).',

# Possible statuses not_open|open|closed
  'cfp_status' : 'open',
  'cfmini_status' : 'open',
  'paper_editing' : 'open',
  'funding_status' : 'not_open',
  'funding_editing' : 'not_open',
  'conference_status': 'not_open',
# Mode
  'cfp_hide_assistance_info': 'no',
  'cfp_hide_scores': 'no',

  'emails': {
     'presentation' : 'speakers@lca2011.linux.org.au',
     'tutorial - 1 hour and 45 minutes'     : 'speakers@lca2011.linux.org.au',
     'tutorial - 3 hours and 30 minutes'    : 'speakers@lca2011.linux.org.au',
     'miniconf'     : 'miniconfs@lca2011.linux.org.au',
     'funding'      : 'funding@lca2011.linux.org.au',
     'poster' : 'speakers@lca2011.linux.org.au'
  },

  'proposal_update_email': 'puck@lca2011.linux.org.au', # recieve notifications when proposals are changed. Leave blank for none.

  'google_map_url': 'http://maps.google.com/maps/ms?ie=UTF8&hl=en&msa=0&msid=117014168848232117270.00048b169407c904d6506',
  'google_map_latlng': '-27.478216,153.019466',
}

lca_rego = {
  'personal_info' : {
      'phone' : 'no',
      'home_address' : 'no',
  },

  'accommodation': {
      # Will delegates be force to organise their own accommodation?
      # set to yes to disable the accommodation questions.
      'self_book': 'no'
  },

  # Set to yes to collect PGP key IDs in rego, no to disable collection.
  'pgp_collection': 'no',

  # Set to no once the conference starts to speed things up
  'confirm_email_address' : 'no',

  'volunteer_areas': (
            {'name': 'Administration', 'description': 'Take care and help out on any administration tasks.'},
            {'name': 'Registration Desk', 'description': 'Sign people into the conference and help with general enquires.'},
            {'name': 'Audio+Video', 'description': 'Help out with filming and/or encoding various talks and presentations.'},
            {'name': 'Network Helper', 'description': 'Assist in setting up and running the network.'},
#            {'name': 'Partners Programme Helper', 'description': 'Help out with the daily activities on the partners programme.'},
            {'name': 'Runner', 'description': 'Move items around, help conference organisers, find things and do general jobs given to you.'},
            {'name': 'Venue Helper', 'description': 'Help with setting up break times, tables and chairs and other miscellaneous things.'},
            {'name': 'Usher', 'description': 'Introduce speakers and manage rooms, keeping them to a schedule.'},
#            {'name': 'Driver', 'description': 'Have driver\'s licence, will travel to help pick up items and shuttle VIP\'s.'},
            {'name': 'Car', 'description': 'Have car and can be a driver, will travel to help pick up items and shuttle VIP\'s.'},
            {'name': 'Week Before', 'description': 'Available during the week before the conference (9-17 Jan).'},
            {'name': 'Week After', 'description': 'Available during the week after the conference (23-31 Jan).'},
            {'name': 'Packout', 'description': 'Available to help pack-out of the venue on Saturday and Sunday.'},
        ),
  'miniconfs' : (
              ('Monday',('Wave Developers', 'Open Programming Languages', 'Business of Open Source', 'Haecksen and Linuxchix', 'Libre Graphics Day', 'Arduino', 'Distro Summit')),
              ('Tuesday',('Launchpad', 'System Administration', 'Open and the Public Sector', 'Education', 'Multimedia', 'Data Storage and Retrieval', 'Multicore and Parallel Computing'))
             ),
  'shells' : ['bash', 'busybox', 'csh', 'dash', 'emacs', 'ksh', 'sh', 'smrsh', 'tcsh', 'XTree Gold', 'zsh'],
  'editors' : ['bluefish', 'eclipse', 'emacs', 'gedit', 'jed', 'kate', 'nano', 'vi', 'vim', 'xemacs'],
  'distros' : ['Arch', 'CentOS', 'Darwin', 'Debian', 'Fedora', 'FreeBSD', 'FreeDOS', 'Gentoo', 'GNU Emacs', 'L4', 'Linspire', 'Mandriva', 'Minix', 'NetBSD', 'Nexenta', 'OpenBSD', 'OpenSolaris', 'OpenSUSE', 'Oracle Enterprise Linux', 'RHEL', 'Slackware', 'Ubuntu', 'Xandros'],
  'past_confs' : [('99', '1999 (CALU, Melbourne)'), ('01', '2001 (Sydney)'), ('02', '2002 (Brisbane)'), ('03', '2003 (Perth)'), ('04', '2004 (Adelaide)'), ('05', '2005 (Canberra)'), ('06', '2006 (Dunedin)'), ('07', '2007 (Sydney)'), ('08', '2008 (Melbourne)'), ('09', '2009 (Hobart)'), ('10', '2010 (Wellington)')],

  'silly_description' : {
        'starts' : ["a", "a", "a", "one", "no"], # bias toward "a"
        'adverbs' : ["strongly",
               "poorly", "badly", "well", "dynamically",
               "hastily", "statically", "mysteriously",
               "buggily", "extremely", "nicely", "strangely",
               "irritatingly", "unquestionably", "clearly",
               "plainly", "silently", "abstractly", "validly",
               "invalidly", "immutably", "oddly", "disturbingly",
               "atonally", "randomly", "amusingly", "widely",
               "narrowly", "manually", "automatically", "audibly",
               "brilliantly", "independently", "definitively",
               "provably", "improbably", "distortingly",
               "confusingly", "decidedly", "historically",
               "shiny", "troublesome"],
        'adjectives' : ["invalid", "valid",
               "referenced", "dereferenced", "unreferenced",
               "illegal", "legal",
               "questionable",
               "alternate", "implemented", "unimplemented",
               "terminal", "non-terminal",
               "static", "dynamic",
               "qualified", "unqualified",
               "constant", "variable",
               "volatile", "non-volatile",
               "abstract", "concrete",
               "fungible", "non-fungible",
               "untyped", "variable",
               "mutable", "immutable",
               "sizable", "minuscule",
               "perverse", "immovable",
               "compressed", "uncompressed",
               "surreal", "allegorical",
               "trivial", "nontrivial"],
        'nouns' : ["pointer", "structure",
               "definition", "declaration", "type", "union",
               "coder", "admin", "hacker", "kitten", "mistake",
               "conversion", "implementation", "design", "analysis",
               "neophyte", "expert", "bundle", "package",
               "abstraction", "theorem", "display", "distro",
               "restriction", "device", "function", "reference",
               "alien"]
    }
}

file_paths = {
  'zk_root' : '/home/zookeepr/zookeepr/lca2011',
  'public_path': '/home/zookeepr/zookeepr/lca2011/zookeepr/public',
  'public_html': '',
  'news_fileprefix': '/home/zookeepr/zookeepr/lca2011/zookeepr/public/featured',
  'news_htmlprefix': '/featured',
  # Points towards where the slides and other recordings are stored
  'slides_path': '/home/zookeepr/zookeepr/lca2011/zookeepr/public/slides',
  'slides_html': '/slides',
  'ogg_path': 'http://mirror.linux.org.au/lca10/videos/ogg',
  'ogg_file_list': '/home/zookeepr/zookeepr/lca2011/zookeepr/config/data.txt',
  'speex_path': 'http://mirror.linux.org.au/lca10/videos/speex',
  'speex_file_list': '/home/zookeepr/zookeepr/lca2011/zookeepr/config/data.txt',
}

lca_menu = [
  ('Home', '/', 'home'),
  ('About', '/about/linux.conf.au', 'about'),
  ('Brisbane', '/brisbane/about', 'brisbane'),
  ('Sponsors', '/sponsors/sponsors', 'sponsors'),
  ('Programme', '/programme/about', 'programme'),
  #('Register', '/register/prices', 'register'),
  #('Register', '/register/prices_ticket_types', 'register'), # -- Stage 4
  ('Media', '/media/news', 'media'),
  ('Contact', '/contact', 'contact'),
  #('Planet', 'http://planet.lca2011.linux.org.au', 'planet'),
  #('Wiki', '/wiki', 'wiki'),
]

lca_submenus = {
  'about': ['linux.conf.au', 'Capital Cabal', 'Venue', 'Map', 'History', 'Linux/Open Source'],
  'brisbane': ['About', 'Map', 'Sightseeing', 'Pre and Post' ],
  'sponsors': ['Sponsors', 'Why Sponsor'],
  #'programme': ['About', 'Social Events', 'Open Day', 'Partners Programme'], # stage 0
  'programme': ['About', 'Keynotes', 'Miniconf Info', 'Presenter FAQ', 'Social Events', 'Open Day', 'Partners Programme'], # stage 1
  #'programme': ['About', 'Keynotes', 'Miniconf Info', 'Papers Info', 'Social Events', 'Open Day', 'Partners Programme'], # stage 2
  #'programme': ['About', 'Keynotes', 'Miniconfs', 'Speakers Info', 'Social Events', 'Open Day', 'Partners Programme'], # stage 2a
  #'programme': ['About', 'Keynotes', 'Miniconfs', 'Schedule', 'Social Events', 'Open Day', 'Partners Programme'], # stage 3
  #'programme': ['About', 'Keynotes', 'Miniconfs','Schedule','Social Events','Open Day', 'Partners Programme'], # stage 4?
  #'register': ['Prices', 'Funding', 'Accommodation', 'Terms and Conditions'],
  #'register': ['Prices/Ticket types','Terms and Conditions','Accommodation','Partners programme'], # stage 4
  'media': ['News','In the press','Graphics']
}

