# 各个IDE的快捷键

IntelliJ Idea无疑是当前最强大的IDE。它提供了各种常用IDE的快捷键映射。 
本程序整理了一份excel，行表示各个IDE，列表示各个命令。   

## IntelliJ Idea的资料来源
IntelliJ的社区版是开源的：https://github.com/JetBrains/intellij-community  
这个repo有以下几个位置比较重要：
* IDE自带的键盘映射
https://github.com/JetBrains/intellij-community/tree/master/platform/platform-resources/src/keymaps  
* IDE全部action列表，在platform/platform-resources/src/idea中有几个与action相关的文件，其中platformAction是最主要的：https://github.com/JetBrains/intellij-community/tree/master/platform/platform-resources/src/idea/ 
* idea的vscode插件：
https://github.com/bulenkov/VSCodeKeymap4IntelliJ/blob/master/resources/keymaps/linux/VSCode.xml

## excel的构建过程
从上述资料中下载到各种xml文件之后，使用Python把xml解析成action到快捷键的映射。然后使用pandas导出为excel。我对excel做了一些美化，包括：
* 固定首行和首列
* 单元格自动换行
* 单元格相邻行颜色不同

## 从excel中得出的结论
* IntelliJ Idea的快捷键设置很不合理，必须自己定制才能好用。萝卜白菜各有所爱，人人都有自己的偏好和个性。
* 各个IDE没有统一的快捷键设置，大部分快捷键没有明确的语义。  
* IDE之间快捷键完全统一是不可能的，不同IDE具有不同的命令、不同的功能。  

# Jetbrain系列keymap文件的写法
keymap可以继承，设置parent即可。keymap是一个平铺的结构，action有id这个属性，表示action的特点，action内部有一个keyboard-shortcut属性。  
```xml
<keymap version="1" name="Eclipse" disable-mnemonics="false" parent="$default">
    <action id="FileChooser.TogglePathShowing">
      <keyboard-shortcut first-keystroke="control P"/>
    </action>
    <action id="$Redo">
      <keyboard-shortcut first-keystroke="control Y"/>
    </action>
    <action id="CopyElement"/>
</keymap>
```