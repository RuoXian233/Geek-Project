# 动画演示思路

1. 展示一段简单的代码

2. 演示编译，解释的共同过程：Lexing
   
    - 提取出源代码中的一句
    - 按词法规则裂开
    - 用不同颜色标注每个 token
    - 收起
    - 结束词法分析的演示

3. 演示编译，解释的共同过程：Parsing

   - 提取出词法序列
   - 遍历词法序列
   - 扫描到关键 token 时给出提示，并绘制树结构，用颜色区分层级
   - 收起 + 总结
   - 结束语法分析的演示
