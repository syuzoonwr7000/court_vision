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

# Vue.js アプリケーションをビルド
RUN npm run build

# ビルドしたファイルを公開
EXPOSE 8080
CMD ["npm", "run", "serve"]
