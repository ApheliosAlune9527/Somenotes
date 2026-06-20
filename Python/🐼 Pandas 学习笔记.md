
## 目录

1. [Pandas 简介与安装配置](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#1-pandas-%E7%AE%80%E4%BB%8B%E4%B8%8E%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE-000000---000222 "null")
    
2. [一维序列 (Series) 深度剖析](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#2-%E4%B8%80%E7%BB%B4%E5%BA%8F%E5%88%97-series-%E6%B7%B1%E5%BA%A6%E5%89%96%E6%9E%90-000222---001314 "null")
    
3. [二维数据框 (DataFrame) 核心构建](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#3-%E4%BA%8C%E7%BB%B4%E6%95%B0%E6%8D%AE%E6%A1%86-dataframe-%E6%A0%B8%E5%BF%83%E6%9E%84%E5%BB%BA-001314---002219 "null")
    
4. [文件导入与多格式数据读取](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#4-%E6%96%87%E4%BB%B6%E5%AF%BC%E5%85%A5%E4%B8%8E%E5%A4%9A%E6%A0%BC%E5%BC%8F%E6%95%B0%E6%8D%AE%E8%AF%BB%E5%8F%96-002219---002719 "null")
    
5. [数据选择与精准索引技术](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#5-%E6%95%B0%E6%8D%AE%E9%80%89%E6%8B%A9%E4%B8%8E%E7%B2%BE%E5%87%86%E7%B4%A2%E5%BC%95%E6%8A%80%E6%9C%AF-002719---003636 "null")
    
6. [布尔过滤与多条件逻辑筛选](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#6-%E5%B8%83%E5%B0%94%E8%BF%87%E6%BB%A4%E4%B8%8E%E5%A4%9A%E6%9D%A1%E4%BB%B6%E9%80%BB%E8%BE%91%E7%AD%9B%E9%80%89-003636---004310 "null")
    
7. [聚合函数与高阶 Groupby 分组统计](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#7-%E8%81%9A%E5%90%88%E5%87%BD%E6%95%B0%E4%B8%8E%E9%AB%98%E9%98%B6-groupby-%E5%88%86%E7%BB%84%E7%BB%9F%E8%AE%A1-004310---005100 "null")
    
8. [核心攻坚：数据清洗 (Data Cleaning)](https://gemini.google.com/app/097e10e69b6e0a16?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all#8-%E6%A0%B8%E5%BF%83%E6%94%BB%E5%9D%9A%E6%95%B0%E6%8D%AE%E6%B8%85%E6%B4%97-data-cleaning-005100---005951 "null")
    

## 1. Pandas 简介与安装配置 `[00:00:00 - 00:02:22]`

### 💡 核心概念

- **什么是 Pandas**：构建在 NumPy 之上、专门用于处理表格数据（Tabular Data）的 Python 库。其名称源于“面板数据（Panel Data）”，它就像是 **Python 版的微软 Excel 增强版**。
    
- **主要数据结构**：
    
    - **Series（序列）**：一维带标签的列（类似于单列电子表格）。
        
    - **DataFrame（数据框）**：二维带标签的网络表格（具有行和列的完整电子表格）。
        

### 📊 结构图解（一维 vs 二维）

```
【Series (一维列)】             【DataFrame (二维表格)】
   Index   Value                Index    Column_A    Column_B
   ┌───┐  ┌─────┐               ┌───┐   ┌────────┐  ┌────────┐
   │ 0 │  │ 100 │               │ 0 │   │ "Spon" │  │   30   │
   ├───┤  ├─────┤               ├───┤   ├────────┤  ├────────┤
   │ 1 │  │ 102 │               │ 1 │   │ "Patr" │  │   35   │
   └───┘  └─────┘               └───┘   └────────┘  └────────┘
```

### 💻 完整命令与代码解析

- **安装指令**：
    
    ```
    pip install pandas
    ```
    
- **模块导入与版本验证**：
    
    ```
    import pandas as pd
    
    # 验证当前 Pandas 版本 (视频演示版本为 2.3.2)
    print(pd.__version__)
    ```
    

## 2. 一维序列 (Series) 深度剖析 `[00:02:22 - 00:13:14]`

### 💡 核心概念

- **一维标记数组**：Series 不仅存储数据，还存储行标签（Index）。
    
- **公寓走廊比喻 (Apartment Hallway)**：走廊就像是一维数据序列，每个房间号就是 **索引（Index / Label）**，房间里的住户就是 **数据（Value）**。
    
- **位置与标签索引**：
    
    - **`.loc` (Location by Label)**：通过自定义的“标签名”精确定位。
        
    - **`.iloc` (Integer Location)**：通过原生 Python 风格的“整数下标（0, 1, 2...）”进行物理定位。
        

### 💻 完整命令与代码解析

- **Series 属性、自定义索引与索引器实战**：
    
    ```
    import pandas as pd
    
    # 1. 从 Python 列表构建 Series
    # 默认索引从 0 开始
    raw_data = [100, 102, 104, 200, 202]
    custom_index = ['A', 'B', 'C', 'D', 'E']
    
    # 注意：Series 首字母大写，代表构造器
    series_obj = pd.Series(raw_data, index=custom_index)
    print(series_obj)
    # 输出包含索引、数据和数据类型 (dtype: int64)
    
    # 2. 定位访问数据
    # 方式 A：通过标签定位 (.loc)
    print("标签 B 对应的值:", series_obj.loc['B'])  # 输出: 102
    
    # 方式 B：通过绝对整数位置定位 (.iloc)
    print("第 0 个物理位置值:", series_obj.iloc[0])  # 输出: 100
    
    # 3. 更新特定值
    series_obj.loc['C'] = 999
    print("更新后的 C 点值:", series_obj.loc['C'])
    
    # 4. 向量化条件过滤
    # 筛选所有值大于或等于 200 的子序列
    filtered_series = series_obj[series_obj >= 200]
    print("过滤后的子序列:\n", filtered_series)
    ```
    
- **趣味实战：使用字典创建日常卡路里追踪器**：
    
    ```
    # 字典的 Key 自动转化为 Series 的 Index (标签)
    calorie_dict = {
        "Day 1": 1750,
        "Day 2": 2100,
        "Day 3": 1700
    }
    
    calories = pd.Series(calorie_dict)
    print("卡路里记录表:\n", calories)
    
    # 更新第三天卡路里 (吃了曲奇，额外增加 500)
    calories.loc["Day 3"] += 500
    
    # 筛选出未达标（摄入超过 2000 卡路里）的暴食天
    overeating_days = calories[calories >= 2000]
    print("超标天数:\n", overeating_days)
    ```
    

## 3. 二维数据框 (DataFrame) 核心构建 `[00:13:14 - 00:22:19]`

### 💡 核心概念

- **多维表格结构**：DataFrame 是由行和列共同组成的网格。每一列本质上都是一个拥有相同索引的 Series。
    
- **数据追加技术变革**：在 Pandas 的现代版本中，原本的 `.append()` 方法已被彻底弃用。**现代推荐的标准做法是使用 `pd.concat()` 进行数据拼接合并**。
    

### 📊 行拼接 (pd.concat) 物理流向

```
【原 DataFrame】                 【新行 DataFrame】
  Index Name Age Job              Index Name Age Job
  ─────────────────              ─────────────────
  Emp1  Spon  30 Cook             Emp4  Sand  28 Engi
          │                                │
          └───────────────┬────────────────┘
                          ▼ pd.concat([df, new_row])
【合并后的新 DataFrame】
  Index Name Age Job
  ─────────────────
  Emp1  Spon  30 Cook
  Emp2  Patr  35 NaN
  Emp3  Squid 50 Cashier
  Emp4  Sand  28 Engi
```

### 💻 完整命令与代码解析

```
import pandas as pd

# 1. 使用字典初始化二维 DataFrame
# 字典中的 Key 对应列名，Value 对应每列的数据列表
employee_data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}
row_labels = ["Employee 1", "Employee 2", "Employee 3"]

df = pd.DataFrame(employee_data, index=row_labels)
print("初始雇员表:\n", df)

# 2. 增加全新的列 (职位)
df["Job"] = ["Cook", "N/A", "Cashier"]
print("增加 Job 列后:\n", df)

# 3. 增加全新的行 (拼接新技术 pd.concat)
# 3.1 先把要添加的新数据打包成一个临时 DataFrame 并指定索引
new_employee = pd.DataFrame({
    "Name": ["Sandy", "Mr. Krabs"],
    "Age": [28, 60],
    "Job": ["Engineer", "Manager"]
}, index=["Employee 4", "Employee 5"])

# 3.2 使用 pd.concat 进行垂直堆叠拼接，合并原 df 与新行 df
df = pd.concat([df, new_employee])
print("合并后的最终雇员表:\n", df)

# 4. 选择性查看行
print("查看 Employee 4 的完整画像:\n", df.loc["Employee 4"])
```

## 4. 文件导入与多格式数据读取 `[00:22:19 - 00:27:19]`

### 💡 核心概念

- **外部数据输入**：Pandas 能够轻松读取包括 `.csv`、`.json`、`.xlsx` 以及 SQL 数据库中的表格数据。
    
- **控制完整输出**：为了不让巨量表格在输出时被省略号截断（默认截取前后 5 行），调用 `.to_string()` 方法可以将整个表格内容以纯文本形式完整打印出来。
    
- **NaN (Not a Number) 占位符**：当数据源中对应格子存在空值时，Pandas 会自动将其填充并显示为 `NaN`。
    

### 💻 完整命令与代码解析

- **读取本地 CSV/JSON 文件（以初代 150 只宝可梦数据为例）**：
    
    ```
    import pandas as pd
    
    # 1. 导入 CSV 文件 (data.csv 与 python 脚本在同级目录)
    # 参数可以是相对路径或绝对物理路径
    df_csv = pd.read_csv("data.csv")
    
    # 2. 导入 JSON 文件
    df_json = pd.read_json("data.json")
    
    # 3. 完整打印控制 (打印 150 只宝可梦的所有行，注意：超大文件请谨慎使用)
    print(df_csv.to_string())
    ```
    

## 5. 数据选择与精准索引技术 `[00:27:19 - 00:36:36]`

### 💡 核心概念

- **指定主键索引列**：在读取 CSV 文件时，通过设置 `index_col='Name'`，可以直接将宝可梦的“名字”作为索引主键。这样便可以直接使用名字作为标签进行定位。
    
- **多列联合过滤**：传入一个包含多个列名的双重括号嵌套列表 `df[['ColA', 'ColB']]`，即可提取出特定的多列子数据集。
    

### 💻 完整命令与代码解析

```
import pandas as pd

# 读取数据，并将 "Name" 列指定为索引，替换默认的 0,1,2... 数字索引
df = pd.read_csv("data.csv", index_col="Name")

# ==================== 列选择 ====================
# 1. 提炼单个列 (返回一维 Series)
print(df["Height"])

# 2. 提炼多列子表 (传入列表，返回二维 DataFrame)
print(df[["Height", "Weight"]])

# ==================== 行选择 (通过 .loc 与 .iloc) ====================
# 1. 查找单行 (直接用宝可梦名称 label 检索)
print("Pikachu 的全部属性:\n", df.loc["Pikachu"])

# 2. 检索某宝可梦的特定属性 (行与列定位组合)
print("Charizard 的身高和体重:", df.loc["Charizard", ["Height", "Weight"]])

# 3. 范围行切片 (查找 Charizard 到 Blastoise 之间的所有宝可梦行)
print(df.loc["Charizard":"Blastoise"])

# 4. 物理范围双轴切片 (.iloc[行物理范围, 列物理范围])
# 获取物理位置第 0 至 10 行，以及第 0 至 3 列
print("前十只宝可梦的部分属性:\n", df.iloc[0:11, 0:3])

# ==================== 命令行交互检索系统实战 ====================
pokemon_input = input("请输入您想查询的宝可梦名称: ").strip()

try:
    # 尝试检索对应行
    print(df.loc[pokemon_input])
except KeyError:
    print(f"❌ 抱歉，宝可梦 '{pokemon_input}' 未在初代 150 图鉴中找到！")
```

## 6. 布尔过滤与多条件逻辑筛选 `[00:36:36 - 00:43:10]`

### 💡 核心概念

- **布尔索引工作流**：将每一行与给定的条件表达式进行比对，保留返回值为 `True` 的行，剔除返回值为 `False` 的行。
    
- **多条件组合守则（极其重要）**：
    
    - 必须使用位运算符：`&` 代表并（And）、`|` 代表或（Or）。
        
    - **绝不能**使用 Python 自带的关键字 `and`/`or`。
        
    - **每个独立的条件表达式必须用圆括号 `()` 括起来**，否则会产生优先级解析错误。
        

### 💻 完整命令与代码解析

```
import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")

# 1. 简单条件筛选：过滤身高在 2 米以上的庞然大物
tall_pokemon = df[df["Height"] >= 2.0]
print("巨型宝可梦数量:", len(tall_pokemon))

# 2. 筛选体重超过 100 kg 且属于传奇级 (Legendary == 1) 的宝可梦
# 注意：使用 C 风格的 & 运算符，并对条件用括号包围
heavy_legendary = df[(df["Weight"] > 100.0) & (df["Legendary"] == 1)]
print("超重传奇宝可梦:\n", heavy_legendary)

# 3. 多元“或 ( | )”逻辑筛选：查找属性一为 Water 或属性二为 Water 的所有水系宝可梦
water_types = df[(df["Type 1"] == "Water") | (df["Type 2"] == "Water")]
print("包含水系基因的宝可梦:\n", water_types)

# 4. 复杂实战：寻找火系 (Fire) 且具有飞行属性 (Flying) 的双系宝可梦 (如喷火龙、火焰鸟)
fire_flying = df[(df["Type 1"] == "Fire") & (df["Type 2"] == "Flying")]
print("火飞双系强者:\n", fire_flying)
```

## 7. 聚合函数与高阶 Groupby 分组统计 `[00:43:10 - 00:51:00]`

### 💡 核心概念

- **数据降维**：聚合函数将巨量数据列缩减为单个统计学汇总值（如均值、最大值等）。
    
- **分类汇总 (`groupby`)**：先将数据集按某一属性（如主要属性 `Type 1`）切分为若干组，再对每一组执行独立的聚合计算（如计算火系、水系等不同组别的平均身高）。
    

### 📊 Groupby 分组计算流向图解

```
【原始表 (按 Type 1 分组)】            【Groupby 计算结果】
  Name       Type 1  Height             Type 1     Height(Mean)
  ─────────────────────             ─────────────────────
  Bulbasaur  Grass    0.7    ──┐
  Oddish     Grass    0.5    ──┼─►  Grass  ──►  (0.7+0.5)/2 = 0.6
  ─────────────────────        │
  Charmander Fire     0.6    ──┼─►  Fire   ──►  (0.6+1.7)/2 = 1.15
  Charizard  Fire     1.7    ──┘
```

### 💻 完整命令与代码解析

- **聚合函数 API 快速检索表**：
    
    |   |   |   |
    |---|---|---|
    |**函数**|**作用**|**补充说明**|
    |`mean(numeric_only=True)`|计算数值列平均值|必须开启 `numeric_only` 排除文本列|
    |`sum(numeric_only=True)`|计算数值列总和|-|
    |`min()`|返回极小值|文本列会按字母 A-Z 顺序返回首项|
    |`max()`|返回极大值|-|
    |`count()`|统计非空（非 NaN）单元格数|初代有 type 2 的只有 67 只，其余为 NaN 不计数|
    
- **代码演示**：
    
    ```
    import pandas as pd
    
    df = pd.read_csv("data.csv", index_col="Name")
    
    # ==================== 全局聚合 ====================
    # 计算所有数值列的均值，numeric_only 确保排除非数值的“属性名”列
    print("各数值列均值:\n", df.mean(numeric_only=True))
    print("总高度和:", df["Height"].sum())
    
    # ==================== 分组聚合 groupby() ====================
    # 1. 按照“主要属性 Type 1”分组
    grouped_by_type = df.groupby("Type 1")
    
    # 2. 计算每个属性分组下的“平均身高”
    avg_height_by_type = grouped_by_type["Height"].mean()
    print("各系平均身高排名:\n", avg_height_by_type.sort_values(ascending=False))
    
    # 3. 统计各系（Type 1）宝可梦的数量 (如水系 28 只，草系极多等)
    pokemon_counts_by_type = grouped_by_type["Height"].count()
    print("各系宝可梦总数:\n", pokemon_counts_by_type)
    ```
    

## 8. 核心攻坚：数据清洗 (Data Cleaning) `[00:51:00 - 00:59:51]`

### 💡 核心概念

- **为什么清洗数据**：**数据分析中 75% 的精力都花在数据清洗上**。真实世界中的原始数据充满了缺失（Missing）、异常（Inconsistent）、重复（Duplicate）以及类型冲突等污点，需要将其清洗后才能送入算法模型。
    
- **清洗核心策略**：
    
    - **丢弃列 (`.drop`)**：去除无关杂质列。
        
    - **删除空值 (`.dropna`)**：去除含有空值（NaN）的记录行。
        
    - **填充空值 (`.fillna`)**：合理代入替代值，保持行数据完整。
        
    - **文本标准化 (`.str`)**：转换大小写等，避免因拼写格式造成统计失效。
        
    - **数据类型转换 (`.astype`)**：将数值列转换为更符合逻辑的布尔型（Boolean）等。
        
    - **去重 (`.drop_duplicates`)**：一键剔除可能污染训练结果的重复冗余行。
        

### 💻 完整命令与代码解析

```
import pandas as pd

# 读入带脏数据的宝可梦表 (此处的 data.csv 尾部已添加了 4 个妙蛙种子和 2 个超梦的重复项)
df = pd.read_csv("data.csv")

# ==================== 1. 剔除无关列 ====================
# 将 'Legendary' 和 'No' 列直接丢弃，该方法返回清洗后的新 DataFrame
df = df.drop(columns=["Legendary", "No"])
print("删除两列后的列结构:\n", df.columns)

# ==================== 2. 缺失值 (NaN) 深度治理 ====================
# 方案 A：直接删去任何 type 2 列存在空值 (NaN) 的宝可梦行
# 此时只会保留双系宝可梦 (150只中仅存 67只)
df_dropped = df.dropna(subset=["Type 2"])
print("执行删除法后剩余行数:", len(df_dropped))

# 方案 B (推荐)：空值填充法，用 "None" 字符串替换 'Type 2' 中的所有 NaN 占位
# 传入一个配置字典，可以指定不同列填充不同的替补值
df = df.fillna({"Type 2": "None"})
print("填充空值后的 Blastoise 信息:\n", df[df["Name"] == "Blastoise"])

# ==================== 3. 纠正异常值 ====================
# 场景：将 'Type 1' 中的所有小写 "grass" 文本标准化替换为全大写 "GRASS"
df["Type 1"] = df["Type 1"].replace({
    "grass": "GRASS",
    "fire": "FIRE",
    "water": "WATER"
})

# ==================== 4. 文本格式标准化 (英文统一小写化) ====================
# 将所有宝可梦的英文名字批量转换为全小写
df["Name"] = df["Name"].str.lower()
print("名字小写化后的前五行:\n", df.head())

# ==================== 5. 重塑/转换数据类型 ====================
# 新增一列 'is_heavy' (重量大于50kg则为1，否则为0)
df["is_heavy"] = (df["Weight"] > 50.0).astype(int)
# 运用 .astype(bool) 将其重塑转换为布尔型 True/False
df["is_heavy"] = df["is_heavy"].astype(bool)
print("修改类型后的前五行:\n", df.head())

# ==================== 6. 重复行去重 ====================
# 场景：一键剔除我们在 data.csv 末尾故意插入的重复 Bulbasaur 和 Mewtwo
original_len = len(df)
df = df.drop_duplicates()
print(f"原数据共 {original_len} 行，去重后剩余 {len(df)} 行，完美恢复至 150 纯净数据！")
```

_祝您 Pandas 数据清洗与挖掘进阶愉快！掌握数据，便掌握了驾驭 AI 时代的魔法钥匙！_