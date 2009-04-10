% if c.printable:
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en-us">
<head>
<title>Tax Invoice/Statement - linux.conf.au 2010</title>
<link rel="icon" type="image/png" href="/images/favicon.ico">
</head>
<body>
% else:
<& actions &>
% #endif

    <h1>Tax Invoice/Statement</h1>

    <div style="text-align:center">
      <h2>Linux Australia Incorporated</h2>
      <p>ABN 56 987 117 479</p>
#NZ GST #90-792-369
    </div>
    <p><strong>Invoice Number:</strong> <% c.invoice.id %></p>
    <p><strong>Invoice Status:</strong> <% c.invoice.status() %></p>
    <p><strong>Issue Date:</strong> <% c.invoice.issue_date.strftime("%d %b %Y") %></p>
    <p><strong>Due Date:</strong> <% c.invoice.due_date.strftime("%d %b %Y") %></p>
% if c.invoice.paid():
    <p><strong>Invoice Paid</strong></p>
% elif c.invoice.total() == 0:
    <p><strong>No Payment Required</strong></p>
% else:
    <p><strong>Amount Due:</strong> <% h.number_to_currency(c.invoice.total()/100.0) %></p>
% #endif

    <p>
      <strong>Attention:</strong> <% c.invoice.person.firstname %> <% c.invoice.person.lastname %>
% if c.invoice.person.registration and c.invoice.person.company:
      <br><strong>Company:</strong> <% c.invoice.person.company %>
% # endif
    </p>

    <p><strong>Regarding:</strong> <% h.event_name() %></p>

    <p>This invoice has been issued as a result of an application to attend <% h.event_name() %>.</p>

    <table style="width: 100%">
      <thead><tr>
        <th>Description</th>
        <th>Qty</th>
        <th>Cost</th>
        <th>Total (Inc. GST)</th>
      </tr></thead>
% for item in c.invoice.items:
      <tr class="<% h.cycle('even', 'odd') %>">
        <td><% item.description %></td>
        <td style="text-align:center"><% item.qty %></td>
        <td style="text-align:right"><% h.number_to_currency(item.cost/100.0) %></td>
        <td style="text-align:right"><% h.number_to_currency(item.total()/100.0) %></td>
      </tr>
% #endfor
      <tr>
        <td style="text-align: right" colspan="3"><strong>Total</strong></td>
        <td style="text-align: right"><strong><% h.number_to_currency(c.invoice.total()/100.0) %></strong></td>
      </tr>
      <tr>
        <td style="text-align: right" colspan="3"><strong>GST Included</strong></td>
        <td style="text-align: right"><strong><% h.number_to_currency(c.invoice.total()/100.0/11) %></strong></td>
      </tr>
    </table>
    
% if not c.invoice.void and c.invoice.paid():
        <p class="pay_button">Invoice has been paid.</p>
% elif c.invoice.bad_payments:
        <p class="pay_button">Invalid payments have been applied to this invoice, please email <% h.contact_email('the organising committee') %></a></p>
% elif not c.invoice.void and not c.invoice.paid():
        <p class="pay_button"><% h.link_to('Pay this invoice', url = h.url(action='pay')) %></p>
% #endif    
    <p>Further information on your registration is available at: <% h.link_to('http://' + h.host_name() + h.url(controller='registration', action='status')(), h.url(controller='registration', action='status')) %></p>

    <p>
      Enquiries may be emailed to the organisers:
% if c.printable:
      <% h.contact_email() %>.
% else:
      <% h.contact_email('contact email') %>.
% #endif
    </p>

    <div style="text-align:center">
      <p><% h.link_to(h.lca_info['event_name'], url=h.lca_info['event_url']) %> is a project of <% h.link_to(h.lca_info['event_parent_organisation'], url=h.lca_info['event_parent_url']) %>.</p>
      <p>
        <% h.lca_info['event_postal_address'] %><br>
        <% h.lca_info['event_tax_number'] %><br>
        Phone: <% h.lca_info['event_phone_number'] %><br>
        Fax: <% h.lca_info['event_fax_number'] %><br>
      </p>
    </div>
% if c.printable:
  </body>
</html>
% #endif

<%method actions>
    <div id="actions">
      <ul>
        <li><% h.link_to('Registration status', url=h.url(controller='registration', action='status')) %></li>
        <li><% h.link_to('Printable version', url=h.url(action='printable')) %></li>
        <li><% h.link_to('PDF version', url=h.url(action='pdf')) %></li>
% if not c.invoice.void and c.invoice.paid():
        <li>Invoice has been paid.</li>
% elif c.invoice.bad_payments:
        <li>Invalid payments have been applied to this invoice, please email <% h.contact_email('the organising committee') %></a></li>
% elif not c.invoice.void and not c.invoice.paid():
        <li><% h.link_to('Pay this invoice', url = h.url(action='pay')) %></li>
        <li>
          <% h.link_to('Regenerate invoice', url = h.url(controller='registration', action='pay', id=c.invoice.person.registration.id)) %>
          <br><span style="font-size: small;">Use the regenerate invoice link if you have edited your registration but the invoice doesn't look quite right.</span>
        </li>
% #endif
      </ul>
%   if 'invoice_message' in h.lca_info:
          <p><small><strong>Please Note:</strong> <% h.lca_info['invoice_message'] %></small></p>
%   #endif
    </div>
</%method>

<%method title>
Tax Invoice/Statement - <& PARENT:title &>
</%method>
