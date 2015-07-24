      <div class="pager">
        <ul class="inline">
          {% if lodspk.offset != 0 %}
          <li class="previous"><a href="{{lodspk.home}}{{lodspk.local.curie|explode:':'|pop}}?limit={{lodspk.limit}}&offset={{lodspk.prev}}">previous</a></li>
          {% endif %}
          <li class="next"><a href="{{lodspk.home}}{{lodspk.local.curie|explode:':'|pop}}?limit={{lodspk.limit}}&offset={{lodspk.next}}">next</a></li>
        </ul>
      </div>
 
