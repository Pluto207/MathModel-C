function result = compare_baseline(baseline, mainValue, direction)
% 比较基线与主模型；direction='min' 或 'max'。
if nargin<3, direction='max'; end
result=struct('baseline',baseline,'main',mainValue,'absolute_change',mainValue-baseline);
if baseline~=0, result.relative_change=(mainValue-baseline)/abs(baseline); else, result.relative_change=NaN; end
if strcmpi(direction,'min'), result.improved=mainValue < baseline; else, result.improved=mainValue > baseline; end
end
