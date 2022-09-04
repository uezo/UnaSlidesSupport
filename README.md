# UnaSlides README

UnaSlidesはVRChatにおけるスライドショー形式のプレゼンテーションシステムです。ワールド外部に用意したプレゼン資料を動的に読み込むことができるため、運営担当者・登壇者双方の負担を大幅に軽減することができます。

特長や機能についてはUnaSlidesの配布ページまたはSpeakerDeckを参照してください。

- https://uezo.booth.pm/items/4141632
- https://speakerdeck.com/uezo/unaslidesnogoshao-jie


# ワールドへの組み込み方法

既存のワールドに組み込んでいただくことができますが、新規作成の場合は以下の通りです。

## 必要リソースのインポート

- VRCSDK3（ワールド用）とUdonSharp v0.20.3をインポート。必ず先にインポートする
- BOOTHからダウンロードしたUnaSlidesのunitypackageをインポート

## オブジェクトの配置

- ヒエラルキーで3D Object > Planeを追加（床の作成）
- VRChat Examples > Prefabs > VRCWorld をヒエラルキーに追加
- UnaSlides > Prefabsから以下のプレファブをヒエラルキーに追加
    - PresentationEngine（プレゼンテーション処理やステータス管理の親玉）
    - MainScreen（スライドを表示するスクリーン）
    - SlideController（スライド操作などを行うためのコントローラー）

## UnaSlidesの設定

ヒエラルキーに配置したオブジェクトを選択し、インスペクターで以下の通り設定します。

NOTE: よくわからない場合は、同梱のExampleシーン（設定済み）を実行してみてください。このヒエラルキーからオブジェクトをコピーしてくることで以下設定を省略することができます。

- PresentationEngine
    - Player: ヒエラルキーのMainScreenオブジェクトをドロップ
    - System Title: 

- MainScreenの設定
    - Engine: ヒエラルキーのPresentationEngineをドロップ
    - MainScreen > Screen > Canvas > Next の On Click() : ヒエラルキーのSlideControllerをドロップして、SendCustomEventを選択し、Nextと入力
    - MainScreen > Screen > Canvas > Back の On Click() : Nextと同様の手順で、Backと入力

- SlideControllerの設定
    - Engine: ヒエラルキーのPresentationEngineをドロップ

以上で設定は終わりです。VRChat SDKのBuild&Test機能を利用して、UnaSlidesを利用できるか試してみましょう。


# プレゼン登壇者の操作方法

- 必ずSlideControllerをPickup（手に持つ）します。これにより操作権限を取得することができます。一度手に持ったらその後は放して構いません
- 各ボタンや入力フィールドの説明は以下の通り
    - [ > ] 次のスライドを表示
    - [ < ] 前のスライドを表示
    - [ >> ] 早送り。1スライド1秒で進行
    - [ Goto... ] 指定した番号のスライドにジャンプ
    - [ Enter URL...] プレゼン資料のURL。入力するとプレゼン資料が読み込まれ、1スライド目を表示
    - [ 1~3 ] カスタムボタン。効果音などの効果やカスタム処理を登録して利用
- スクリーンの右側をレイキャストで選択することにより次のスライド、左側を選択することで前のスライドを表示

NOTE: プレゼン中に他人がSlideControllerをPickupしてしまうと、プレゼンの操作権限を失います。取り戻すことで操作を再開できますが、オーディエンス含め他人がPickupしないように管理してください。


# プレゼン資料の作成方法

VRChatでは外部動画の再生が可能なため、プレゼン資料を動画形式で作成。

## 仕様

- スライド割り当て: 1スライド1秒。FPSは問わない
- 動画形式: 問わないが、YoutubeなどVRChatがサポートする動画サイトで利用できる形式。検証はYoutubeにてMP4で実施
- 品質: 問わないが、UnaSlides標準のスクリーンは720p

## 作成方法

- PowerPointの場合、ファイル > エクスポート でMP4形式を選択。継続時間を1秒に設定して保存すればOK
- Google SlidesやPDFの場合、1スライド1画像の形式で出力したのち、動画に変換。以下のPythonスクリプトを実行することで変換可能。後日使いやすい形で提供予定

以上
