function [ok, violations] = check_constraints(x, lb, ub, A, b, Aeq, beq, tol)
% 检查常见线性/边界约束；不替代题目专用约束。
if nargin < 8 || isempty(tol), tol=1e-8; end
violations=struct('lower',[],'upper',[],'ineq',[],'eq',[]);
violations.lower=find(x < lb-tol); violations.upper=find(x > ub+tol);
if nargin>=4 && ~isempty(A), violations.ineq=find(A*x > b+tol); end
if nargin>=6 && ~isempty(Aeq), violations.eq=find(abs(Aeq*x-beq)>tol); end
ok=isempty(violations.lower)&&isempty(violations.upper)&&isempty(violations.ineq)&&isempty(violations.eq);
end
