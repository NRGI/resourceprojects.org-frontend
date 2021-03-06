    <table class="table table-striped" about="{{uri}}">
    <thead>
      <tr><th>Subject</th><th>Predicate</th><th>Object</th></tr>
    </thead>
    {% for row in models.po %}
     <tr>
<td>{%if forloop.first%}<a href='{{lodspk.this.value}}'>{{lodspk.this.curie}}</a>{%endif%}</td>
     <td><a href='{{row.p.value}}'>{{row.p.curie}}</a></td>
     
        <td>
        {%if row.o.uri == 1%}
        <a rel='{{row.p.value}}' href='{{row.o.value}}'>{{row.o.curie}}</a>
        {%else%}
        <span property='{{row.p.value}}'>{{row.o.value}}</span>
        {%endif%}
        </td>

        </tr>
    {% endfor %}

    {% for row in models.sp_reduced %}
      <tr>
        <td><a href='{{row.s.value}}'>{{row.s.curie}}</a></td>

        <td><a rev='{{row.s.value}}' href='{{row.p.value}}'>{{row.p.curie}}</a></td>
<td>{%if forloop.first%}<a href='{{lodspk.this.value}}'>{{lodspk.this.curie}}</a>{%endif%}</td>
        </tr>
    {% endfor %}

    </table>
