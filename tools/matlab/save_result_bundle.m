function manifest = save_result_bundle(outputDir, problem, cfg, result, check)
% 数模C MATLAB 结果固化：MAT、TXT、JSON 三种可追溯输出。
if ~exist(outputDir, 'dir'), mkdir(outputDir); end
manifest = struct();
manifest.schema_version = '1.1';
manifest.problem = problem;
manifest.model_version = get_field(cfg, 'model_version', 'unversioned');
manifest.result_version = get_field(cfg, 'result_version', manifest.model_version);
manifest.random_seed = get_field(cfg, 'seed', NaN);
manifest.matlab_version = version;
manifest.timestamp = char(datetime('now','Format','yyyy-MM-dd HH:mm:ss'));
manifest.result_status = get_status(result);
manifest.validation_status = get_status(check);
manifest.output_dir = outputDir;
manifest.result_summary = summarize_struct(result);
manifest.validation_summary = summarize_struct(check);
save(fullfile(outputDir, [problem '_bundle.mat']), 'cfg', 'result', 'check', 'manifest');
write_text_manifest(outputDir, problem, manifest);
write_json_manifest(outputDir, problem, manifest);
end
function v=get_field(s,name,default)
if isstruct(s) && isfield(s,name), v=s.(name); else, v=default; end
end
function s=get_status(x)
if isstruct(x) && isfield(x,'status'), s=char(string(x.status)); else, s='UNKNOWN'; end
end
function out=summarize_struct(x)
out=struct();
if ~isstruct(x), out.type=class(x); return; end
names=fieldnames(x);
for i=1:numel(names)
 n=names{i}; v=x.(n);
 if ischar(v) || isstring(v) || islogical(v) || (isnumeric(v) && isscalar(v))
  out.(matlab.lang.makeValidName(n))=v;
 end
end
end
function write_text_manifest(outputDir,problem,m)
fid=fopen(fullfile(outputDir,[problem '_manifest.txt']),'w'); c=onCleanup(@()fclose(fid));
fprintf(fid,'schema_version=%s\nproblem=%s\nmodel_version=%s\nresult_version=%s\nrandom_seed=%g\nmatlab_version=%s\nresult_status=%s\nvalidation_status=%s\ntimestamp=%s\n',string(m.schema_version),string(m.problem),string(m.model_version),string(m.result_version),m.random_seed,string(m.matlab_version),string(m.result_status),string(m.validation_status),string(m.timestamp));
end
function write_json_manifest(outputDir,problem,m)
text=jsonencode(m);
fid=fopen(fullfile(outputDir,[problem '_manifest.json']),'w'); c=onCleanup(@()fclose(fid)); fwrite(fid,text,'char'); fprintf(fid,'\n');
end
