import pandas as pd

def to_(df, f_t, f_n):
    try:
        if f_t==".csv":
            df.to_csv(f_n+f_t, sep="\t", index=0)
        elif f_t==".xlsx":
            df.to_excel(f_n+f_t, sep="\t", index=0)
    except:
        print("失败")
    else:
        print("成功")
    finally:
        pass

def read_(f_name, f_n_t):
    if f_n_t=="xlsx":
        return pd.read_excel(f_name)
    elif f_n_t in ["csv","txt"]:
        return pd.read_csv(f_name, sep="\t", header=0)
    else:
        pass

if __name__ == "__main__":
    f_name = input("文件名：")
    t_f = input("保存类型.xxx:")
    f_n_list = f_name.split(".")

    try:
        df = read_(f_name, f_n_list[-1])
        print(df)
    except:
        print("读取失败")
    else:
        to_(df, t_f, f_n_list[0])
    finally:
        pass