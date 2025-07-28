# 2025 睿能-福大企业实训嵌入式软件作业

```cpp
typedef struct tagFileBUFFER            //存花样名称
{
    CHAR FileName[64];
    INT32S Enable;                  //当前花样是否有效
    INT32S TotalSockNum;     //目标件数
    INT32S CurSockNum;       //已织件数
    INT32S CycleSet;		 //循环次数
    INT32S CycleCur;		 //已循环次数
    INT32S LuoWwNum;		 //缝头落袜产量
    INT32S LostNum;		 	//废片产量
    INT32S fileRow;                     //花样在第几列
    INT32S Bak[6];
}FileBUFFER, *PFileBUFFER;

struct KNIT_SEQU_PARA
{
    //编织计划
    FileBUFFER SequFileName[MAX_SEQU_FILE];   //文件名 30*50
    INT32S SequFileSn;          //当前花型序号
    INT32S SequKnitEn;         //使能
    INT32S SequKnitLastSn;

    INT32S Bak[2048-1500-3];
    KNIT_SEQU_PARA()
    {
        memset(this,0,sizeof(KNIT_SEQU_PARA));
        SequKnitLastSn = 1;
    }
};
```

## 任务：

**1.编写启动应用脚本，上电自动执行应用程序。(10分)**
**2.自行调研json库，将KNIT_SEQU_PARA结构体转换为 JSON 格式存储(50分)**
**3.结构体中添加任意类型变量时，JSON转换过程应当非常方便，不需要复杂的修改(40分)**

## 验收：

**项目验收报告**：涵盖学习感悟，项目实现方案、代码和效率（执行 JSON 格式存储所花时间）。
