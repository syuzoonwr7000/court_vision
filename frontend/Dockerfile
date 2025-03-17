# ベースイメージとして Node.js を使用
FROM node:16

# 作業ディレクトリを指定
WORKDIR /app

# package.json と package-lock.json をコピー
COPY package.json /app
COPY package-lock.json /app

# 依存関係をインストール
RUN npm install

# アプリケーションコードをコピー
COPY ./src /app/src

# 開発サーバー用にポートを開放
EXPOSE 8080

# 開発サーバーを実行
CMD ["npm", "run", "serve"]
