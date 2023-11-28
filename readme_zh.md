### [English Version](./readme_en.md)

### 设置:

1. **安装**:
   - 安装 Flask-Migrate: `pip install flask-migrate`
   - 安装 Flask-Mail: `pip install flask-mail`
   - 安装 Flask-WTF: `pip install flask-wtf`
   - 安装 Email Validator: `pip install email_validator`

2. **数据库迁移**:
   - 初始化迁移: `flask db init`
   - 生成迁移: `flask db migrate`
   - 应用迁移: `flask db upgrade`

### [进行的步骤](#email-verification-and-database)

#### 设置电子邮件验证:

1. **Flask-Mail 配置**:
   - 在应用的配置中配置电子邮件
   - 在扩展中初始化 Flask-Mail
   - 在 `auth.py` 中创建发送邮件的视图函数
   - 测试邮件功能

2. **电子邮件验证和数据库**:
   - 在数据库中存储验证代码（修改模型）
   - 实现数据库更改的三步迁移
   - 以 JSON 格式实现电子邮件验证的 AJAX 响应

3. **前端实现**:
   - 更新 HTML 路径
   - 集成前端的 AJAX
   - 实现验证倒计时功能

### [表单验证](#user-authentication)

1. **Flask-WTF 设置**:
   - 使用 Flask-WTF 创建表单验证
   - 使用 Email Validator 包进行电子邮件验证

### [用户身份验证](#question-and-answer-functionalities)

1. **登录页面后端**:
   - 修改数据库登录表的表单
   - 更新身份验证函数
   - 实现会话和登录功能的秘钥

2. **钩子和身份验证**:
   - 在 `app.py` 中实现两个钩子函数
   - 在已登录和未登录状态之间切换

3. **注销功能**:
   - 创建注销页面的视图函数

### [问答功能](#troubleshooting-css-loading-issues)

1. **创建问答视图和页面**:
   - 实现发布问题和答案的视图函数和 HTML 页面
   - 修改问答功能的模型
   - 实现用于发布问题的验证用户登录状态的装饰器

2. **渲染问答模板**:
   - 更新 `index.html` 和问答模块中的相应视图函数
   - 修改问答部分的头像图片

3. **实现问答列表页**:
   - 更新 `detail.html` 和问题详情的视图函数
   - 实现从主页到问题详情页的导航

4. **解决 CSS 加载问题**:
   - 确认 CSS 文件加载问题
   - 通过在 `base.html` 中使用 `url_for` 替代相对路径解决

### [答案模型和修正](#submission-error-correction)

1. **解决数据库表创建问题**:
   - 解决数据库表创建错误的问题
   - 删除数据库和迁移，然后重新创建解决问题

2. **模型修正**:
   - 修正 'author' 字段的模型问题

3. **密码字段长度调整**:
   - 解决密码字段长度限制导致服务器错误的问题
   - 在模型中修改密码字段长度并执行迁移

4. **提交错误修正**:
   - 修正视图函数中缺失的 'return' 语句导致的提交错误

5. **实现答案提交**:
   - 后端：验证提交答案的表单和视图函数
   - 前端：更新详情页面以渲染答案列表

6. **搜索功能**:
   - 后端：在问答模块中实现搜索功能
   - 前端：更新基础 HTML 以支持搜索功能

### [其他任务](#project-completion)

- 改进提交信息和记录先前修复的错误
- 撰写 Markdown 文档的英文版

### [项目完成](#中文版)

- 通过实现所有功能完成项目
- 视频教程: [链接](https://www.bilibili.com/video/BV17r4y1y7jJ?p=41&vd_source=1a0df84062fc3afe05ddb5436ffce988)
- GitHub 仓库: [链接](https://github.com/MUC-NBM/zlktqa)

这个结构化的中文版文档提供了项目步骤和解决的问题的详细概述，同时包含了导航链接以便快速访问特定部分。