# FLStudioSysEx
How to send System Exclusive command by using FL Studio
<img width="1920" alt="fl4" src="https://user-images.githubusercontent.com/4214168/158175316-37ef37cb-4ae0-4d72-8f8e-d6c6127bf046.png">

Basically I aligned with https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm

Please read "The basics of working with Script Files:"
According to this explanation, I made device_CASIO CTSV1000.py and put into \\Documents\Image-Line\FL Studio\Settings\Hardware\CASIO CTS1000V\

The Script set OnInit() for initialization. I put change Lylic Play Mode of CTS-1000V to "NOTE" from "Phrase(default)"

You may want to send SysEX every play cycle. For that purpose, it can use onUpdateBeatIndicator(), this can call every beat while playing.

------------------------
FL Studioを使ったシステムエクスクルーシブの送信

リファレンスマニュアル（https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm）のMIDI Scriptingを用いてDevice APIを用いて行います。

The basics of working with Script Filesに書かれていることに沿って行いますが、英語なので、ざっくり和訳します。
まず初めに、scriptファイルをつくる必要があります。FL StudioのUser dataフォルダに置きます。

- フォルダを作ります。例えば、'...Documents\Image-Line\FL Studio\Settings\Hardware\YourScriptSubFolder'です。ここでYourScriptSubFolderは、お好きな名前（通常は接続するMIDI楽器名でしょうか。）にします。
- スクリプトファイルを作ります。作ったフォルダの中にメモ帳かなにかで、'device_YourScriptName.txt'というファイルを作ります。ファイル名の先頭はdevice_にしないといけません。
このファイルの最初の行に、# name=My First Scriptという行を書きます。My First Scriptというところは、FL StudioのMIDI Settings > Controller type list:に表示されます。

ファイル名の拡張子をtxtからpyに変えます。'device_ThisIsMyFistScript.txt' から 'device_ThisIsMyFistScript.py'のような感じです。.py拡張子をテキストエディタに関連付けしてもいいでしょう。
MIDI Settingsを開くと、MIDI Settings > Controller type listに、この例に沿うと My First Script (user)という項目が増えています。

FL StudioのVIEW メニュー > Script output > Edit script (ボタン)を押すと、スクリプトを編集できます。

今回は、CASIO CTS-1000V用に、'device_CASIO CTSV1000.py'というファイルを作りました。\\Documents\Image-Line\FL Studio\Settings\Hardware\CASIO CTS1000V\に置いています。このスクリプトは、起動されると、OnInit()が呼ばれて、CTS-1000Vのボイスシンセサイザ部のLylic Play Modeをディフォルトの"Phrase"から"NOTE"に変更します。

onUpdateBeatIndicator()にも同様のコマンドをコメントで書いていますが、これはサンプルです。もし再生中の拍ごとになにかエクスクルーシブを送りたい場合、ここに記載するとよいでしょう。


