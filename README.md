# Django ToDo app
- class Based View で作成していく
### django のテンプレートとCRUD
- C : Create (作成する)
- R : Read (読み込む『情報を取る』)
- U : Update (更新する)
- D : Delete (削除する)
  - Twitter, Facebook, メルカリ などの具体的な service 内容は上記ように集約できるのではないか
  - 概ね上記の4つを意識して作成すれば主要な機能は集約できるのではないか
### django と CRUD の繋がり
- C : Create (作成する)
  - Create View
- R : Read (読み込む『情報を取る』)
  - List View
  - Detail View
- U : Update (更新する)
  - Update View
- D : Delete (削除する)
  - Delete View
### 1. 今回は末尾に " . " (ドット)を付ける
    django-admin startproject todoproject .
- " . " (ドット)を付ける事で、指定した project の中に必要な file が作成される
### 2. アプリ作成
    python manage.py startapp todo
- todo app
### 3. project の settings.py file の初期設定
- TEMPLATES で 'DIRS': [BASE_DIR / 'templates'], 記述
- manage.py file と同じ階層に templates directory 作成
  - mkdir templates
### 4. settings.py に app を作成した事を記述する
- INSTALLED_APPS に 'todo.apps.TodoConfig', を記述
  - 頭文字を大文字とConfig を忘れずに
### 5. project urls.py file に path 追加
- path(' ', include('todo.urls')),　
- include method も import する
  -  '  ' に admin 以外が入った場合に、いかなる場合でも app の url を呼び出す
### App の中に urls.py file 作成する
- path admin だけを残しておく
## models.py について
- Excel、スプレットシートのような表計算ソフト
  - data を効率的に扱う事ができる仕組み
  - django においてdatabase を使用する際に間を取り持つ役割が models.py
  - database をうまく活用する為の設計図
### 5. database DB (データベース) に table を作成する
- データベースマネイジメントシステム
  - data をうまく活用するための方法論
### makemigrations と migrate
- models.py file を作成しただけでは table は作成されない
- makemigrations, migrate を入力すると DB に table ができる
#### なぜ２つのコマンドがあるのか？
- 順番は、makemigrations -> migrate を行う
- **migrate** は実際にDB に書き込んでいって、table を作成するコマンド
- **makemigrations**は、models.py に基づいて設計図を作成する
  - なぜ、models.py と makemigrations の2つの設計図が必要なのか？
  - models.py はdataが上書きされてしまう為、変更した履歴詳細を残しておかないと後々の修正や開発が大変な為
  - makemigrations があると database に書き込む前にerror があった場合、error があるとアドバイスをくれる
### 5-1. makemigrations コマンド実行
    python manage.py makemigrations < app名 >
- app名を指定しないと、ECサイトの場合などは沢山の app があるので変更があった場合に全て一気に反映されてしまって分かりづらくなってしまう
### 5-2. migrate コマンドを実行
    python manage.py migrate
- Applying todo.0001_initial... OK
  - todo.0001 を基に database に書き込みをしました、できました。
###  6. terminal で 全ての data を扱える superuser を作成
    python manage.py createsuperuser
- name, email, password を新規作成して管理画面でログインすることができる
### 6-1. server へ
    python manage.py runserver
- http://127.0.0.1:8000/admin/ でログイン画面へ
- 先ほど作成した name, password 入力でログイン
- ログインして database へアクセスできる
### 6-2. app(Todoapp) の admin.py file (django) に 指定の data を扱うという指示を記述
- admin.site.register(Todomodel)
  - 管理画面に対して登録する（Todomodel）を登録
## CRAD の考え方を使用して View 作成
### List View (読み込む「情報を取る」)
- data の一覧を list として表示する事に適したテンプレート
### Django が備えている タグ
- html file に記述できる django 独自のタグ
  - {{  }} : data を扱う際に使用される
    - どの object のどの フィールドの値を表示するのかを記載するタグ
  - {% %} : 複雑な処理
    - python でいう for文とか if文を行う際に用いられるタグ
### DetailView (読み込む「情報を取る」)
- 個別の data を表示する事に
- data の中身を表示する事に適したテンプレート
## base.html のテンプレートを繰り返し使用する
- base.html とは？
  - それぞれの code に当てはめて行く為に、違う html file の中身を当て込んで行く為の枠組みを作っていく
- Block を指定していく
  - Block header
  - Block sidebar
  - Block content
  - Block footer
### base.html を他の html に読み込む
    {% extends 'base.html' %}
- 共通して使用できる code 共有の為に読み込み
- base.html を使用する事によって簡単に枠組みを共有できる
- bootstrap のサイトを見ながら、site を作成していく
> https://getbootstrap.jp/
## 優先度によって色を変えていく
- user が data を作成するときに指定するもの
- 事前に明確に決める事ができない
- models.py の中で user が選択できるように何かしらフィールドを追加していく
### choices を使用してtext 入力ではなく選択肢を与える
- choices = < 変数名（CHOICE）> : 変数名は大文字にする事
- 変数は tuple 形式で記述していく
  - CHOICE = (("danger", "high"), ("warning", "normal"), ("primary", "low"))
    - 上記は Bootstrap を使用しているの danger, warning, primary などの指定でスタイルが反映される
    -  ※ あくまでの一例
    - ( UIの色 , 選択肢 ) -> ("赤色で表示", "最優先")
### models.py を編集後は下記のコマンドを実施
    python manage.py makemigrations
- 必須入力項目やエラー、注意喚起が出た場合はそのコメントにしたがって対応する
- 全て完了すると新規で migrations file が作成される
### 上記後に下記コマンドを実施
    python manage.py migrate
- 上記で DB に書き込みが完了する
### runserver で /admin で確認
    python manage.py runserver
- http://127.0.0.1:8000/admin/ で選択肢と日付が作成されているか確認する
## Create View (作成する)
- データを新しく作るときに適したテンプレート
1. App 内の urls.py file に path を通す
   - from improt を忘れずに
   - class Based View なので、 .as_view( ) も記述
2. App 内の views.py file に class 作成 Create View 継承
   - template の html（使用するhtml を指定
   -  model (作成したdata をどこに保存するか) を指定
   -  ※ model の指定をしないと django はどこに data を保存していいかわからなくなる
3. template directory 内に create.html 作成 base.html を extends する
   - block content 作成。create.html 内で表示させる html を記述していく
   - from と input  html で記述 ※ 今回は from 内の method = 'POST' を使用
   - POST -> from などの data を送るときに使用する method
   - get -> default で web サイトなどの訪問などに使用する method
4. django テンプレート記述 {{ form.as_p }} を記載
   - {{ form.as_p }} を記載するだけで form を実装できる
   - as_p　->　{{ form.as_p }} will render them wrapped in < p > tags
   - formの中を htmlの < p > で囲って表示（記述）してくれる
   - https://docs.djangoproject.com/en/3.2/topics/forms/
5. Create View を使用するには **fileds** をしてしないといけない
   - App の views.py file に表示させる フィールドを記述していく
   - 表示させるフィールドは、models.py に記述したモノ
6. create.html の form に {% csrf_token %} を追記
   - < form action="" method="POST" >{% csrf_token %}
   - セキュリティー対策の仕様
7. data が作成された後にどの page に移行するのかを指示を記載
   - App views.py file に記述する
   - success_ulr =revese_lazy(' list ')
   - revese_lazy を import する
     - from jango.urls import reverse_lazy
     - 分からない場合は django ドキュメントで検索
  - success_ulr は data が作成された場合に遷移させる url を示している
   - revese_lazy は django の正しい流れが逆になる
     - 正しい流れとは リクエスト -> レスポンスまでの一連の流れ
     - リクエスト -> urls.py -> views.py -> models.py -> views.py -> レスポンス
   - （' 引数 '）を基準として逆に回していく
     - App の urls.py file の path に name=" 引数 " として記載していく
     - path("list/", TodoList.as_view(), name="list"),
 - data が作成されたときに reverse_lazy("list") が呼び出されて、list という url に対応した url に遷移させる事ができる
 - revese_lazy は、dataが保存された後に実行されるモノ
## Delete View (削除する)
- data を削除するときに適したテンプレート
1.  を通す（url の繋ぎ込み）
   - TodoDelete imoport (delete url を受けることによって、TodoDelete を呼び出す)
   - 複数の data がある中で削除する data を特定する必要があるので < int:pk > を指定して、どの data を削除していくかを指定する必要がある
2. views.py に class 作成。Delete View 継承
   - ここもcreta view と同じく template = delete.html 作成
   - model = "  "  model の指定 ※ どの model data を削除するのかを記載しないと django が理解できない為
   - success_url = revese_lazy（" 遷移先 "） を指定 ※ 削除してしまったらその data が完全に無くなってしまうので、どの page に遷移させるのかを記述する
   - Delete View を import
3. temlpat directory 内に delete.html を作成
   - urls.py paht で,< int:pk > を指定しているので記述は、form の html だけでOK
## Update View (更新する)
- データを更新んする時に適したテンプレート
1. update も intger 型のプライマリキーをとてくる
   - 複数の data がある中で update する data を特定する必要があるので < int:pk > を指定して、どの data を update していくかを指定する必要がある
2. 流れは create と delete 同じ
## url タグ設定
- a href="{% url ' ' %}" で指定する : django の便利機能
  - a href="　" に直接 link を書き込む事もできるが、直書きは推奨されていない
  - 変更があった場合に一気に変えることができない
- a href="{% url ' name ' %}" でやっている事、仕組みは reverse と同じ
  - name は urls.py file で指定した name=" ◯◯ "
- {% url ' ' %} に引数を設定する必要がある
  - 個別の object の番号
  - 上記を指定しないと django はどの data を削除・編集すればいいのか分からない
  - ＜int:pk ＞ : intger 型 の プライマリキーも一緒に投げてあげる
  - 入れる場所は url の name の後に記述
  - object名.pk　->　a href="{% url ' update ' item.pk %}"
### django ドキュメント
> https://docs.djangoproject.com/ja/3.2/ref/templates/builtins/
## Todo App まとめ
- model(makemigrations, migrate)
  - DB と django をつないでいく為に 2つのコマンドを打ち込んでいく
- 管理画面
  - django が備えている非常に便利な機能
  - それぞれの user を作成して、かつ data を編集したり作成したりできる
- Base.html
  - テンプレートを使用して共通部分の見た目を共有させる
  - 中に Block content などを作成して 表示させる内容を入れ込んでいく
- CRUD とそれぞれのview
  - CRUD を元にして django が作成している事を理解する
  - それぞれの view の昨日と dajngo 便利な class を備えている
- Csrf_token, reverse, pk
  - セキュリティー対策として django が default で備えているもの
  - Form を作成する場合には、上記を入れないと error になってしまう
  - reverse : 名前からview を呼び出す
  - pk : プライマリキー　DBにおいて重複しない data (番号)がふられている
  - pk を使用する事によって意図している data を持ってくることができる
