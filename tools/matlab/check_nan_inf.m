function ok = check_nan_inf(x, name)
% 返回变量是否不含 NaN/Inf；失败时打印位置。
if nargin < 2, name = 'value'; end
bad = ~isfinite(x);
ok = ~any(bad(:));
if ~ok, idx=find(bad); fprintf(2,'%s contains NaN/Inf at linear indices: %s\n',name,mat2str(idx(1:min(10,end)))); end
end
