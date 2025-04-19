import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# ページ設定 (最初に解除して全体設定を確認しましょう)
# ============================================
st.set_page_config(
    page_title="Streamlit デモ",
    layout="wide", # wide にすると中央だけでなく画面幅いっぱいに表示されます
    initial_sidebar_state="expanded" # デフォルトでサイドバーを開いた状態にします
)

# ============================================
# アプリケーションのタイトルと説明
# ============================================
st.title("✨ Streamlit 初心者向けインタラクティブデモ ✨")
st.markdown("### Streamlitの機能を体験しましょう")
st.markdown("""
このデモは、Streamlitの基本的なUI要素、レイアウト、データ表示、グラフ表示などをすべて表示しています。
各要素がどのように表示されるか確認してください。
""")

# ============================================
# サイドバー
# ============================================
st.sidebar.header("📘 デモの表示内容")
st.sidebar.markdown("""
このアプリは、以下のStreamlit機能をデモしています。

-   基本的なUI要素 (テキスト入力, ボタン, チェックボックス, スライダー, セレクトボックス)
-   レイアウト (カラム, タブ, エクスパンダー)
-   データ表示 (データフレーム, テーブル, メトリクス)
-   グラフ表示 (ラインチャート, バーチャート)
-   インタラクティブ機能 (プログレスバー, ファイルアップロード)
-   スタイルのカスタマイズ (カスタムCSS)

コード (`app.py`など) を確認して、それぞれの機能がどのように実装されているか見てみましょう。
""")
st.sidebar.info("コードを変更して、Streamlitの可能性を探求してみてください！")


# ============================================
# 基本的なUI要素
# ============================================
st.header("🧩 基本的なUI要素")
st.markdown("テキスト入力、ボタン、チェックボックスなど、ユーザーとのインタラクションに使う基本的な部品です。")

# テキスト入力
st.subheader("✏️ テキスト入力 (st.text_input)")
name = st.text_input("あなたの名前を入力してください", "ゲスト")
st.write(f"こんにちは、{name}さん！")

# ボタン
st.subheader("🖱️ ボタン (st.button)")
if st.button("ここをクリックしてください"):
    st.success("ボタンがクリックされました！ 🎉")

# チェックボックス
st.subheader("✅ チェックボックス (st.checkbox)")
if st.checkbox("チェックを入れると追加コンテンツが表示されます"):
    st.info("チェックボックスがオンになりました！このテキストが表示されています。")

# スライダー
st.subheader("🎚️ スライダー (st.slider)")
age = st.slider("あなたの年齢を選択してください", 0, 100, 25)
st.write(f"選択された年齢: {age}歳")

# セレクトボックス
st.subheader("🔽 セレクトボックス (st.selectbox)")
option = st.selectbox(
    "好きなプログラミング言語を選んでください",
    ["Python", "JavaScript", "Java", "C++", "Go", "Rust", "Ruby"]
)
st.write(f"あなたが選んだ言語は {option} です。")

# ============================================
# レイアウト
# ============================================
st.header("📐 レイアウト")
st.markdown("画面の表示領域を分割したり、要素をグループ化したりする方法です。")

# カラム
st.subheader("カラムレイアウト (st.columns)")
col1, col2 = st.columns(2) # 2つのカラムを作成
with col1:
    st.write("### 左側のカラム")
    st.image("https://via.placeholder.com/150?text=Left", caption="左の画像")
with col2:
    st.write("### 右側のカラム")
    st.image("https://via.placeholder.com/150?text=Right", caption="右の画像")


# タブ
st.subheader("タブ (st.tabs)")
tab1, tab2, tab3 = st.tabs(["🐱 ねこ", "🐶 いぬ", "🐰 うさぎ"])

with tab1:
    st.write("ねこに関する情報です...")
    st.image("https://via.placeholder.com/300?text=Neko")

with tab2:
    st.write("いぬに関する情報です...")
    st.image("https://via.placeholder.com/300?text=Inu")

with tab3:
    st.write("うさぎに関する情報です...")
    st.image("https://via.placeholder.com/300?text=Usagi")


# エクスパンダー
st.subheader("エクスパンダー (st.expander)")
with st.expander("ここをクリックすると詳細が表示されます"):
    st.write("""
        この部分はデフォルトでは折りたたまれており、クリックすると展開されます。
        たくさんの情報をコンパクトにまとめたいときに便利です。
    """)
    st.success("詳細が表示されました！")


# ============================================
# データ表示
# ============================================
st.header("📊 データの表示")
st.markdown("データフレームやテーブル、数値などのデータを整形して表示します。")

# サンプルデータフレームを作成
df = pd.DataFrame({
    '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤', '山田', '小林'],
    '年齢': [25, 30, 22, 28, 33, 29, 26],
    '都市': ['東京', '大阪', '福岡', '札幌', '名古屋', '東京', '大阪']
})

# データフレーム表示
st.subheader("データフレーム (st.dataframe)")
st.markdown("フィルタリングやソートが可能なインタラクティブな表です。")
st.dataframe(df, use_container_width=True) # use_container_width=True で横幅をコンテナに合わせる

# テーブル表示
st.subheader("テーブル (st.table)")
st.markdown("静的なシンプルな表です。")
st.table(df)

# メトリクス表示
st.subheader("メトリクス (st.metric)")
st.markdown("主要な数値とその増減を分かりやすく表示します。")
col1, col2, col3 = st.columns(3)
col1.metric("売上", "120万円", "5%")
col2.metric("ユーザー数", "3,500人", "-2%")
col3.metric("満足度", "4.5/5", "0.2")


# ============================================
# グラフ表示
# ============================================
st.header("📈 グラフの表示")
st.markdown("簡単なコードでデータからグラフを生成できます。")

# ラインチャート
st.subheader("ラインチャート (st.line_chart)")
chart_data = pd.DataFrame(
    np.random.randn(20, 3), # 20行3列のランダムデータ
    columns=['A', 'B', 'C'])
st.line_chart(chart_data)

# バーチャート
st.subheader("バーチャート (st.bar_chart)")
chart_data_bar = pd.DataFrame({
    'カテゴリ': ['A', 'B', 'C', 'D', 'E'],
    '値': np.random.randint(10, 100, 5) # 10から100のランダムな整数を5つ
}).set_index('カテゴリ')
st.bar_chart(chart_data_bar)


# ============================================
# インタラクティブ機能
# ============================================
st.header("🚀 インタラクティブ機能")
st.markdown("ファイルのアップロードやプログレスバーなど、ユーザー操作に関連する機能です。")

# プログレスバー
st.subheader("プログレスバー (st.progress)")
st.markdown("タスクの進捗状況を表示する際に便利です。")
progress_label = st.empty() # ラベル表示用のプレースホルダー
progress_bar = st.progress(0) # プログレスバー本体

if st.button("進捗シミュレーションを開始"):
    for i in range(101):
        time.sleep(0.02) # 少し待つ
        progress_label.text(f"進捗: {i}%") # ラベルを更新
        progress_bar.progress(i) # プログレスバーを更新
    st.balloons() # 完了したらバルーンを表示
    progress_label.text("完了しました！")


# ファイルアップロード
st.subheader("ファイルアップロード (st.file_uploader)")
st.markdown("ユーザーにファイルをアップロードしてもらいたいときに使います。")
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"]) # CSVファイルのみを受け付ける

if uploaded_file is not None:
    # ファイルのデータを表示
    file_details = {"FileName":uploaded_file.name, "FileType":uploaded_file.type, "FileSize":uploaded_file.size}
    st.write(file_details)

    try:
        # CSVの場合はデータフレームとして読み込む
        df_uploaded = pd.read_csv(uploaded_file)
        st.write("アップロードされたCSVデータのプレビュー:")
        st.dataframe(df_uploaded.head())
    except Exception as e:
         st.error(f"ファイルの読み込み中にエラーが発生しました: {e}")


# ============================================
# カスタマイズ
# ============================================
st.header("🎨 スタイルのカスタマイズ")
st.markdown("マークダウンやカスタムCSSで表示を調整できます。")

# カスタムCSS
st.subheader("カスタムCSS (st.markdown with unsafe_allow_html=True)")
st.markdown("""
<style>
.big-font {
    font-size: 24px !important;
    font-weight: bold;
    color: #ff4b4b; /* Streamlitのエラー表示に近い赤 */
}
.highlight {
    background-color: yellow;
    padding: 5px;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">これはカスタムCSSで文字を大きく、赤くしたテキストです！</p>', unsafe_allow_html=True)
st.markdown('これは<span class="highlight">ハイライトされた</span>テキストです。', unsafe_allow_html=True)


# ============================================
# デモの終わり
# ============================================
st.divider() # 区切り線
st.markdown("### これでStreamlit初心者向けデモは終了です。")
st.markdown("様々な機能を試して、あなた自身のStreamlitアプリ開発に役立ててください！")
st.info("ご不明な点があれば、いつでも質問してください。")