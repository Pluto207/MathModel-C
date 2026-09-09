# MATLAB-first 计算规范

## 主入口

每问使用 `求解/问题X/main_qX.m` 作为唯一主脚本；从项目根目录启动，不依赖 MATLAB 工作区残留变量。主脚本依次完成：初始化路径 → 读取数据 → 预处理 → 建模 → 求解 → 验证 → 保存结果 → 生成图表。

## 函数化目录

```text
问题X/
├── main_qX.m
├── read_data.m
├── preprocess_data.m
├── build_model.m
├── solve_model.m
├── validate_model.m
├── plot_results.m
└── results/
```

## MATLAB 优先级

1. 基础 MATLAB、矩阵运算、ODE、插值、拟合和自编小规模算法；
2. 已确认可用的 Optimization/Statistics/Global Optimization 工具箱；
3. Python 仅用于特殊文件格式、论文检查或 MATLAB 无法稳定覆盖的辅助任务。

## 必查项

- `ver` 和所需工具箱许可；
- 行列维度、单位、NaN/Inf、缺失值和异常值；
- 随机算法固定 `rng(seed)`；
- 优化解的约束可行性；
- 物理模型的量纲、边界、初值、守恒量和时间/空间步长；
- 结果导出 CSV/MAT/JSON，并写入模型版本、参数、种子和输入摘要。

## 结果固化

在主程序中优先调用 `save_result_bundle(outputDir, problem, cfg, result, check)`，并把返回的 manifest 与结果一起保存。结果发生实质变化后，复现清单、主张—证据表和论文摘要数字退回 REVIEW/DRAFT。

## 最小运行门

正式全量计算前，必须用小数据或等价小实例完成：读取 → 预处理 → 求解 → 一个关键指标 → 一张结论图 → 保存文件。
