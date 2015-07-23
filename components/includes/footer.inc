  <footer>
    <div class="container">
      <div class="strapline">
          <p>The Natural Resource Governance Institute promotes the effective, transparent and accountable management of oil, gas and mineral resources for the public good.</p>
      </div>
      <div class="row">
        <div class="col-md-4">
            <h2 class="block-title">ResourceProjects.org</h2>
            <p>This site is a prototype, based on under-contributed data. No warranty of the accuracy or completeness of data is provided, and users should always check against original sources before making decisions based upon the data presented here. 
            </p>
            <p>
            Unless otherwise stated, all data on the the site is available as open data under <a href="https://creativecommons.org/licenses/by-sa/4.0/legalcode">Creative Commons License CC-BY-SA</a>.   
            <p>
            <p>
            Errors and omissions can be reported to: <a href="mailto:apedersen@resourcegovernance.org">apedersen@resourcegovernance.org</a>
            </p>
        </div>
        <div class="col-md-4">
          <h2 class="block-title">Advanced</h2>
          <ul class="list-unstyled">
            <li><a href="{{lodspk.home}}classes">Classes</a></li>
              <li><a href="{{lodspk.home}}namedGraphs">Named Graphs</a></li>
          </ul>
        </div>
        <div class="col-md-4">
               <h2 class="block-title">Links</h2>
               <ul class="list-unstyled"><li><a href="http://www.resourcegovernance.org/">Natural Resource Governance Institute (Main Website)</a></li></ul>         
        </div>
      </div>
    </div>
  </footer>
  <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
  <script src="//netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
  <script src="//cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.13.3/jquery.tablesorter.min.js"></script>
  <script src="//cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.13.3/jquery.tablesorter.widgets.min.js"></script>
  <script>$(function() { $("table.table").tablesorter(); });</script>
  <script type="text/javascript" src="{{lodspk.home}}js/bootstrap3-typeahead.js"></script>
  <script type="text/javascript">
  $(document).ready(function(){
      $('.typeahead').typeahead({
          source: function (query, process) {
            $('.typeahead').addClass('wait');
            return $.get('{{lodspk.home}}search/'+encodeURIComponent(query), { }, function (data) {
                $('.typeahead').removeClass('wait');
                return process(data);
            }, 'json');
          },
          afterSelect: function (obj) {
            $('.typeahead').attr('disabled', true);
            window.location = obj.uri;
          },
          displayText: function(item){ return item.value;}
      });
  });
  </script>
  </body>
</html>
