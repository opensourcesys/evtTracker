# 事件跟踪器 #

* Author: Joseph Lee, Thiago Seus

此插件输出有关为其触发事件的对象的信息。在调试日志模式中记录的属性包括对象类型、名称、角色、事件、应用程序模块和可访问性 API 特定信息，例如
IAccessible 对象的 accName 和 UIA 对象的自动化 Id。

注意：

* 此插件专为需要跟踪来自应用程序和各种控件事件的开发者和高级用户而设计。
* 为了使用此插件，NVDA 必须在调试模式下进行日志记录（从常规设置/日志记录级别进行配置，或在启用调试日志记录的情况下重新启动）。
* 在 Event Tracker 之前运行的插件可能无法将事件传递给其他插件，包括 Event
  Tracker。如果发生这种情况，事件跟踪器将无法记录事件。
* 事件按顺序从全局插件、应用程序模块、树拦截器和 NVDA 对象处理。

## 事件及其信息

跟踪和记录以下事件：

* 焦点操作：获得焦点、失去焦点、进入焦点、前景
* 更改：名称、值、状态、描述、实时区域
* 其他事件： alert
* UIA 事件：控制器、拖放、元素选择、项目状态、布局无效、通知、系统警报、文本更改、工具提示打开、窗口打开

对于每个事件，将记录以下信息：

* 事件名称
* 对象
* 对象名称
* 对象角色
* 取决于事件的对象值或状态
* 应用模块
* 对于 IAccessible 对象：acc 名称、子 ID
* 对于 UIA 对象：Automation
  Id、类名、通知属性（如果记录通知事件信息）、布局无效事件的子对象数量、项目状态的属性、拖拽和放置（如果已定义）

您还可以指定一个手势以在列表中查看事件（NVDA 菜单选项/按键与手势，事件跟踪器类别）。该列表最多保存 100 个已处理的最新事件。

If you find this add-on useful, please [review it][1] in the NVDA Add-on
Store.

## Version 25.1.0

* NVDA 2025.1 compatibility.
* NVDA 2024.1 or later is required due to Python 3.11 upgrade.
* Restored limited support for Windows 8.1.
* Made the add-on code more robust with help from Pyright (a Python static
  type checker).
* NVDA will record actual control role name instead of integers when
  reporting events.

## Version 24.1.0

* NVDA 2024.1 compatibility.
* opensourcesys/evtTracker #4: the first event's description no longer
  missing when first opening the event viewer. Contributed by: WangFeng
  Huang (hwf1324)

## 版本 23.02

* 需要 NVDA 2022.4 或更高版本。
* 需要 Windows 10 21H2（2021 年 11 月更新/内部版本 19044）或更高版本。
* 将跟踪 Alert 事件（主要针对 IAccessible 对象）。

## 版本 23.01

* 需要 NVDA 2022.3 或更高版本。
* 需要 Windows 10 或更高版本，因为自 2023 年 1 月起，Microsoft 不再支持 Windows 7、8 和 8.1。

## 版本 22.12

* 添加了事件列表对话框（未分配手势）以列出插件记录的最多 100 个最近的事件（By Thiago Seus）。
* UIA 通知属性等其他事件信息与事件同时被记录。

## 版本 22.10

* 出于安全考虑，需要 NVDA 2022.2 或更高版本。
* 跟踪以下 UIA 属性更改：拖拽、放置。
* UIA 项目状态属性文本已记录。
* 如果对象没有定义窗口类名，NVDA 将不再播放错误提示音或无任何动作。

## 版本 22.06

* 出于安全考虑，需要 NVDA 2021.3 或更高版本。

## 版本 21.10

* 由于对 NVDA 的更改会影响此插件，因此需要 NVDA 2021.2 或更高版本。
* UIA 布局无效事件将被跟踪。
* 对象角色和状态信息将类似于最近 NVDA 版本中的开发者信息。

## 版本 21.07

* 初始发行。

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
