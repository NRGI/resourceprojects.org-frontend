
      <div class="pager">
        <ul class="inline">
          {% if lodspk.offset != 0 %}
          <li><a href="{{lodspk.home}}data/{{lodspk.args.arg0}}?limit={{lodspk.limit}}&offset={{lodspk.prev}}">previous</a></li>
          {% endif %}
          <li><a href="{{lodspk.home}}data/{{lodspk.args.arg0}}?limit={{lodspk.limit}}&offset={{lodspk.next}}">next</a></li>
        </ul>
      </div>
 
