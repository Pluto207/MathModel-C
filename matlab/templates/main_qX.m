function main_qX()
% 数模C MATLAB 主入口模板
% 从项目根目录调用：run('求解/问题X/main_qX.m')
% 请勿依赖 base workspace 中的变量。

clc;
close all;
format long g;

projectRoot = fileparts(fileparts(fileparts(mfilename('fullpath'))));
addpath(genpath(fullfile(projectRoot, '求解', '问题X')));

cfg = struct();
cfg.problem = 'X';
cfg.model_version = 'v0.1';
cfg.seed = 42;
cfg.output_dir = fullfile(projectRoot, '结果');
cfg.figure_dir = fullfile(projectRoot, '图表');
if ~exist(cfg.output_dir, 'dir'), mkdir(cfg.output_dir); end
if ~exist(cfg.figure_dir, 'dir'), mkdir(cfg.figure_dir); end
rng(cfg.seed, 'twister');

% TODO: 替换为题目数据与模型合同中的真实参数。
data = read_data_placeholder(projectRoot);
model = build_model_placeholder(data, cfg);
result = solve_model_placeholder(model, cfg);
check = validate_model_placeholder(model, result, cfg);

save(fullfile(cfg.output_dir, 'qX_result.mat'), 'cfg', 'data', 'model', 'result', 'check');
write_summary_placeholder(cfg, result, check);
plot_placeholder(cfg, data, result);

fprintf('qX finished: model=%s, seed=%d\n', cfg.model_version, cfg.seed);
end

function data = read_data_placeholder(projectRoot)
data = struct('source', fullfile(projectRoot, '数据', 'TODO'));
end

function model = build_model_placeholder(data, cfg)
model = struct('data_source', data.source, 'version', cfg.model_version);
end

function result = solve_model_placeholder(model, cfg)
result = struct('status', 'PLACEHOLDER', 'seed', cfg.seed, 'model', model.version);
end

function check = validate_model_placeholder(~, result, ~)
check = struct('status', 'TODO', 'result_status', result.status, ...
    'baseline_compared', false, 'constraints_checked', false, ...
    'units_checked', false, 'sensitivity_checked', false);
end

function write_summary_placeholder(cfg, result, check)
fid = fopen(fullfile(cfg.output_dir, 'qX_summary.txt'), 'w');
cleanup = onCleanup(@() fclose(fid));
fprintf(fid, 'status=%s\n', result.status);
fprintf(fid, 'validation=%s\n', check.status);
end

function plot_placeholder(cfg, ~, ~)
fig = figure('Visible', 'off');
plot(nan, nan);
title('Replace with a conclusion-bearing figure');
exportgraphics(fig, fullfile(cfg.figure_dir, 'result_qX_placeholder.png'), 'Resolution', 300);
close(fig);
end
