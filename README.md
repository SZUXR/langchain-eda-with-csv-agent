# 💡 CSV数据分析智能工具

基于LangChain和Streamlit构建的智能CSV数据分析工具，支持自然语言查询和数据可视化。

## 🚀 功能特性

- **智能数据分析**: 使用自然语言描述您的数据分析需求
- **多种可视化**: 支持条形图、折线图、散点图
- **交互式界面**: 基于Streamlit的用户友好界面
- **AI驱动**: 集成OpenAI GPT-4模型进行智能数据解读
- **CSV文件支持**: 轻松上传和分析CSV格式数据

## 📋 系统要求

- Python 3.8+
- OpenAI API密钥

## 🛠️ 安装步骤

1. **克隆项目**
```bash
git clone <your-repository-url>
cd langchain-eda-with-csv-agent
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **准备示例数据**（可选）
```bash
python prepare_data.py
```

## 🎯 使用方法

1. **启动应用**
```bash
streamlit run app.py
```

2. **配置API密钥**
   - 在侧边栏输入您的OpenAI API密钥
   - 获取API密钥：[OpenAI API Keys](https://platform.openai.com/account/api-keys)

3. **上传数据**
   - 点击"上传你的数据文件（CSV格式）"
   - 选择您要分析的CSV文件

4. **开始分析**
   - 在文本框中用自然语言描述您的分析需求
   - 例如：
     - "显示里程数最多的前10位乘客"


## 📊 支持的查询类型

### 文字回答
- 数据统计问题
- 趋势分析
- 异常值检测

### 表格展示
- 数据筛选和排序
- 分组统计
- 汇总报告

### 图表可视化
- **条形图**: 适合分类数据比较
- **折线图**: 适合时间序列分析
- **散点图**: 适合相关性分析

## 📁 项目结构

```
langchain-eda-with-csv-agent/
├── app.py              # 主应用程序
├── utils.py            # 工具函数和AI代理
├── prepare_data.py     # 示例数据准备脚本
├── requirements.txt    # 项目依赖
└── README.md          # 项目文档
```

## 🔧 核心组件

- **app.py**: Streamlit主界面，处理文件上传和用户交互
- **utils.py**: 包含LangChain代理配置和数据处理逻辑
- **prepare_data.py**: 生成示例数据集（出租车数据）

## 💡 使用示例

```python
# 示例查询
"提取passengers和distance两列"
"绘制不同支付方式的使用频率条形图"
"分析行程距离与车费的关系散点图"
```

## ⚠️ 注意事项

- 确保CSV文件格式正确，包含列标题
- API密钥会在会话期间保存，但不会永久存储
- 大型数据集可能需要较长的处理时间
- 建议数据文件大小不超过100MB

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！



## 🆘 常见问题

**Q: 如何获取OpenAI API密钥？**
A: 访问 [OpenAI平台](https://platform.openai.com/account/api-keys) 注册账户并创建API密钥。

**Q: 支持哪些文件格式？**
A: 目前仅支持CSV格式文件。

**Q: 可以分析多大的数据文件？**
A: 建议文件大小不超过100MB，以确保良好的性能表现。