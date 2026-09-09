function report = check_matlab_env(requiredToolboxes)
% 数模C MATLAB 环境预检。只检查，不安装或修改系统。
if nargin < 1, requiredToolboxes = {}; end
report = struct();
report.matlab_version = version;
report.platform = computer;
report.required_toolboxes = requiredToolboxes;
report.toolboxes = struct();
for i = 1:numel(requiredToolboxes)
    name = requiredToolboxes{i};
    field = matlab.lang.makeValidName(name);
    report.toolboxes.(field) = license('test', name);
end
report.base_functions = struct('readtable', exist('readtable','file') == 2, ...
    'writetable', exist('writetable','file') == 2, ...
    'exportgraphics', exist('exportgraphics','file') == 2, ...
    'fmincon', exist('fmincon','file') == 2, ...
    'ode45', exist('ode45','file') == 2);
report.timestamp = char(datetime('now','Format','yyyy-MM-dd HH:mm:ss'));
disp(report);
end
