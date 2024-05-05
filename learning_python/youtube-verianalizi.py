import pandas as pd

df = pd.read_csv("GBvideos.csv")
result = df

# ilk 10 kaydı getirme
result = df.head(10)

# ikinci 5 kaydı getirme
result = df[5:15].head()

# datasetde bulunan kolon isimlerini getirme
result = df.columns

# datasetde bulunan kolonların sayıları
result = len(df.columns)

# datasetten kolon silme
df.drop(["thumbnail_link","comments_disabled","ratings_disabled"],axis=1,inplace=True)  #inplace yazılmazsa ya da False olursa yeni bir DataFrame döner ve silme işlemi gerçekleşmez.
result = df

# video beğenme ve beğenmeme sayılarının ortalamasını bulma
result = df["likes"].mean()
result = df["dislikes"].mean()

# ilk 50 videonun like ve dislike kolonlarını getirme
result = df.head(50)[["title","likes","dislikes"]]

# en çok görüntülenen video
result = df[df["views"].max() == df["views"]][["title","views"]]

# en fazla görüntülenen ilk 10 video
result = df.sort_values("views",ascending=False).head(10)[["title","views"]]

# kategoriye göre beğeni ortalamalarını sıralı bir şekilde getirme
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# kategoriye göre yorum sayılarının toplamı
result = df.groupby("category_id").sum()

# her kategoride kaç video vardır
result = df["category_id"].value_counts()

# en popüler video beğeni sayısına göre










print(result)







