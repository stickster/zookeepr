<h2>Welcome to MyLCA!</h2>

<p>
Welcome, <strong><% c.person.firstname %></strong>!
</p>

<p>
This is... MyLCA!
</p>

<div id="submissions">

<p>Your current list of submissions:
<ul>

% for s in c.person.submissions:
<li>
<% h.link_to(s.title, url=h.url(controller='submission', action='view', id=s.id)) %>

<span class="actions">
[
<% h.link_to('edit', url=h.url(controller='submission', action='edit', id=s.id)) %>
|
<% h.link_to('delete', url=h.url(controller='submission', action='delete', id=s.id)) %>
]
</span>

</li>
% #endif

</ul>

</p>

<p>
<% h.link_to('submit another', url=h.url(controller='submission', action='new')) %>
</p>

</div>
