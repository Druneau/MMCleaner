% rebase('layout.tpl', title=title, year=year)
<h2>{{ title }}</h2>
<h3>Short Term</h3>
<div class="row">
  % for item in shortTerm:
  %   if item == shortTerm[0]:
        <div class="col-md-2">
        <h5>{{item}}</h5>
  %   elif item.split()[0] in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        </div>
        <div class="col-md-2">
        <h5>{{item}}</h5>
  %   elif 'Snow' in item:
        <li><b>{{item}}</b></li>
  %   elif item.split()[0] in ['Temp:', 'Rain:']:
        <li>{{item}}</li>
  %   end 
  % end
        </div>
</div>
<h3>Long Term</h3>
<div class="row">
  % for item in longTerm:
  %   if item == longTerm[0]:
        <div class="col-md-2">
        <h5>{{item}}</h5>
  %   elif item.split()[0] in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        </div>
        <div class="col-md-2">
        <h5>{{item}}</h5>
  %   elif 'Snow' in item:
        <li><b>{{item}}</b></li>
  %   elif item.split()[0] in ['High:', 'Low:', 'Rain:']:
        <li>{{item}}</li>
  %   end 
  % end
        </div>
</div>


