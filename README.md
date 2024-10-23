# 課題
## FlaskでSwitchBotAPIを叩くAPIを実装

### 課題概要

この課題では、**PythonのFlaskフレームワーク**を使い、SwitchBotAPIにアクセスする基本的なAPIを自分で実装してもらいます。APIとは何か、どのように通信を行いデータを取得するのかを体験することが目的です。SwitchBotのデバイス情報を取得・操作する実装を通じ、APIの仕組みを理解しましょう。

---

### 1. 事前準備

#### 1.1 GitHubアカウントの作成
1. [GitHub](https://github.com) にアクセスし、「Sign up」をクリック。
2. ユーザー名、メールアドレス、パスワードを入力し、アカウントを作成。
3. 届いた確認メールの指示に従い、メールアドレスを確認。

#### 1.2 gitのインストール
1. [git公式サイト](https://git-scm.com/) から「Download for Windows」をクリック。
2. インストーラーを実行し、デフォルト設定のままインストール。
3. インストール後、コマンドプロンプトで以下を実行し、gitが動作することを確認。
   ```bash
   git --version
   ```

#### 1.3 Docker Desktopのインストール
1. [Docker Desktop](https://www.docker.com/products/docker-desktop) からWindows版をダウンロード。
2. インストーラーを実行し、案内に従いインストール。
3. インストール後、Docker Desktopを起動し、タスクトレイにクジラのアイコンが表示されることを確認。

4. **WSL 2** のバックエンドを有効にする必要がある場合、以下を確認してください：
   - [Windows Subsystem for Linuxのインストール](https://learn.microsoft.com/en-us/windows/wsl/install)
   - PowerShellで次を実行：
     ```bash
     wsl --install
     ```
### 2. 環境構築

#### 2.1 任意のディレクトリに移動
コマンドプロンプトまたはPowerShellで、プロジェクトを配置するディレクトリに移動します。
例：
```bash
cd C:\Users\YourName\Projects
```

#### 2.2 リポジトリのクローン
以下のコマンドで、リポジトリをクローンします。
```bash
git clone https://github.com/KuRa04/switchbot-flask-api-practice.git
```

#### 2.3 Visual Studio Codeでプロジェクトを開いて、拡張機能をダウンロード
1. VisualStudioCodeを起動し、「ファイル」→「フォルダを開く」でクローンしたリポジトリのフォルダを選択してください。
2. VisualStudioCodeの「拡張機能」を選択し、「REST Client」と検索してください。
3. 検索欄にある「REST Client」をインストールしてください。[REST Clientのインストール方法](https://qiita.com/mgmgmogumi/items/61f0b896580d3e6db2bb)
4. インストールしたREST Clientを反映させるためにVisualStudioCodeを再起動してください。


#### 2.4 Dockerコンテナの起動
VSCodeのターミナルを開き、以下のコマンドでDockerコンテナを立ち上げます。
初回は`--build`オプションが必要です。
```bash
docker-compose up --build
```

#### 2.5 動作確認
以下のURLにアクセスし、「hello flask」というテキストが表示されたら動作確認完了です。
-  [http://localhost:8080/](http://localhost:8080/)
---

## 課題1: Flaskで基本的なAPIエンドポイントを作成する

**問題**

まずはFlaskを使って簡単なAPIを作成しましょう。以下の仕様に従って`/hello`というエンドポイントを実装してください。

- `GET /hello` にアクセスしたときに、`{"message": "Hello, World!"}` というJSONが返るようにする。

**ヒント**

- `Flask`の`app.route()`を使います。
- `jsonify()`関数を使うと、PythonのdictをJSON形式に変換できます。

---

## 課題2: SwitchBotAPIを叩いてデバイス一覧を取得する

**問題**

SwitchBotAPIの`/devices`エンドポイントにアクセスして、デバイス一覧を取得する処理を実装してください。以下の仕様に従い、`/devices`というエンドポイントを作成します。

- **HTTPメソッド**: POST
- **入力**: JSON形式で`token`と`secret`を受け取る。
    
    ```json
    {
      "token": "your_token_here",
      "secret": "your_secret_here"
    }
    
    ```
    
- **処理**:
    - 取得した`token`と`secret`で認証ヘッダーを生成し、SwitchBotAPIの`https://api.switch-bot.com/v1.1/devices`にGETリクエストを送信。
    - 取得したデバイスの一覧を返す。

**ヒント**

- `requests`ライブラリを使って外部APIにアクセスします。
- `generate_api_header`関数を再利用できます。

---

## 課題3: デバイスのステータスを取得するAPIの作成

**問題**

SwitchBotの特定デバイスのステータスを取得するためのAPIを実装してください。以下の仕様に従って`/device/status`というエンドポイントを作成します。

- **HTTPメソッド**: POST
- **入力**: JSON形式で`token`、`secret`、および`device_id`を受け取る。
    
    ```json
    {
      "token": "your_token_here",
      "secret": "your_secret_here",
      "device_id": "your_device_id_here"
    }
    
    ```
    
- **処理**:
    - `device_id`に対応するデバイスのステータスをSwitchBotAPIから取得。
    - デバイスのステータス情報をJSONで返す。

**ヒント**

- APIのURLは`https://api.switch-bot.com/v1.1/devices/{device_id}/status`です。

---

## 課題4: デバイスのコマンドを実行する

**問題**

SwitchBotのデバイスにコマンドを送信するエンドポイントを実装してください。以下の仕様で`/device/command`というAPIを作成します。

- **HTTPメソッド**: POST
- **入力**: JSON形式で`token`、`secret`、`device_id`、および実行する`command`を受け取る。
    
    ```json
    {
      "token": "your_token_here",
      "secret": "your_secret_here",
      "device_id": "your_device_id_here",
      "command": {
        "command": "turnOn",
        "parameter": "default",
        "commandType": "command"
      }
    }
    
    ```
    
- **処理**:
    - 指定されたデバイスに対して、送信されたコマンドを実行。
    - 実行結果をJSON形式で返す。

**ヒント**

- コマンドを実行するAPIのURLは`https://api.switch-bot.com/v1.1/devices/{device_id}/commands`です。

---

## 課題5: エラーハンドリングを実装する

**問題**

課題2~4のAPIでは、SwitchBotAPIが失敗する可能性があります（例: 無効なトークン）。エラーが発生した場合、HTTPステータスコードやエラーメッセージを正しく処理して返してください。

**要件**:

- SwitchBotAPIが`400`や`401`エラーを返したとき、同じステータスコードとエラーメッセージをフロントエンドに返すこと。

**ヒント**

- `response.status_code`を使ってSwitchBotAPIのレスポンスのステータスを取得できます。

---

### 提出方法

- 修正したファイルをGitHubにPushし、自分の親ブランチにPullRequestを作成
    - 作業ブランチの作成方法
        - mainからブランチ名: `feature/学生番号` を切る
            - 例：s1923010の場合、`feature/s1923010`
        - `feature/s1923010` を親ブランチとして、課題毎にブランチを切る
            - 例：課題1の場合、`feature/s1923010` →`feature/s1923010-task-1`

- SwitchBotAPIのトークンとシークレットはハードコードせず、POSTリクエストのJSONから受け取る形にしてください。

---

この課題を通じて、**APIの基礎的な実装手法**、**Flaskの使い方**を学べます。
また、エラーハンドリングを通じて、API実装の課題にも触れることができます。