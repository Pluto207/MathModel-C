function out = run_sensitivity(values, evaluator)
% values 为 N×1 或 N×K 参数矩阵；evaluator 为 @(row) 指标函数。
if isempty(values), out=[]; return; end
n=size(values,1); y=zeros(n,1);
for i=1:n, y(i)=evaluator(values(i,:)); end
out=struct('parameters',values,'metric',y,'min',min(y),'max',max(y),'range',max(y)-min(y));
end
