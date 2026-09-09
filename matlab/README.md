# 数模 C MATLAB 模板

## 使用

将 `templates/main_qX.m` 复制到实际项目的 `求解/问题X/main_qX.m`，再按模型合同替换占位函数。占位模板不会产生科学结论；在正式运行前必须删除 `TODO/PLACEHOLDER` 并通过 R 门。

## 入口约定

从项目根目录运行：

```matlab
run('求解/问题1/main_q1.m')
```

每个问题的入口必须自行设置路径、参数和随机种子，不能依赖 base workspace。
