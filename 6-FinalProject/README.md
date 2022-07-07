# BrainFuck Interpreter 
A usable implement by C++17.  
 [BrainFuckとは？](https://en.wikipedia.org/wiki/Brainfuck) 

これはBrainFuck言語の完全な実装で、オリジナルの構文に、私が個人的にDebugに有益だと思う機能を追加しています。  
そして、完全なターミナルユーザーインターフェイスがあります。


### 使い方：
このソフトウェアを使うのに、CMakeのインストールが必要である。

Build手順：
1. gitでこのプロジェクトをcloneする：
```bash
>>> git clone https://github.com/MuxFox/2022-SystemDevelopCourse
```

2. 6-FinalProject ホルダーを開く：
```bash
>>> cd 2022-SystemDevelopCourse
2022-SystemDevelopCourse>>> cd 6-FinalProject
```

3. build ホルダーを作る
```bash
6-FinalProject>>> makedir build
```

4. CMakeでbuild
```bash
6-FinalProject>>> cd build
build>>> cmake ..
```

5. CMakeで作ったMakeFile経由でCompile
```bash
build>>> make .
```

ここまでできたら、Executableファイルはbuildホルダーにあるはず、使ってみる：

```bash
build>>> BrainFuck -v
Mux BrainFuck Interpreter, CopyRight: Mux 2022
[Compiler and C++ Version used to build BrainFuck: clang++/std:201703]
Version: 1.0.2
```