```mermaid
graph TD;
    A[打开 APT 攻击武器检测特征库平台] --> B[在 C++ 环境下运行平台]
    B --> C[加载测试用例 (test 规则库)]
    C --> D[进入 Feature Editor（特征编辑器）]
    D --> E[右键新建 "文本属性（Text）" 特征]
    E --> F[填写特征信息: Key=childcommandlinecontain, Content=stratum+tcp://]
    F --> G[点击 "保存 (Save)" 按钮, 创建特征]
    G --> H[进入规则模块栏, 添加规则]
    H --> I[进入 Feature Rule Editor（特征规则编辑器）]
    I --> J[右键添加 "AND 关系" 作为根规则]
    J --> K[添加子规则 1 || 2 || 3]
    K --> L[右键 AND 规则 -> 选择 "添加规则"]
    L --> M[在 OR 规则下添加特征1, 特征2, 特征3]
    J --> N[添加子规则 !4]
    N --> O[右键 AND 规则 -> 选择 "添加规则"]
    O --> P[添加特征4, 并设为 "NOT"]
    P --> Q[选择 update 更新特征库并保存]
    Q --> R[进入 "特征匹配界面"]
    R --> S[选择输入方式: 文本, Hex, 或样本文件]
    S --> T[输入文本 "this is a test word" 进行匹配]
    T --> U{匹配结果?}
    U -- 否 --> V[显示未匹配]
    U -- 是 --> W[显示匹配成功]
    V --> X[选择添加待匹配样本]
    X --> Y[点击 "Match" 按钮, 进行匹配分析]
    Y --> W
    W --> Z[点击设置按钮, 进入系统配置]
    Z --> ZA[选择语言, 进行国际化设置]
    ZA --> ZB[确认选择后, 平台自动重启]
    ZB --> ZC[完成语言切换]
    ZC --> ZD[使用 "保存" 或 "保存至" 选项]
    ZD --> ZE[存储特征及规则至本地文件]
    ZE --> ZF[可重新加载, 确保匹配一致性]
