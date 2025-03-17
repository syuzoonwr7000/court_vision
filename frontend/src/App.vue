<template>
  <div id="app">
    <h1>テニスの試合分析</h1>
    
    <!-- ファイル選択ボタン -->
    <div class="file-upload">
      <label for="file-input" class="upload-label">ローカルからファイルを選択</label>
      <input type="file" id="file-input" @change="handleFileChange" />
    </div>
    
    <!-- YouTube URL入力欄 -->
    <div class="youtube-url">
      <label for="youtube-url" class="youtube-label">YouTubeURL</label>
      <input type="url" id="youtube-url" v-model="youtubeUrl" placeholder="YouTubeのリンクを貼ってください" />
    </div>
    
    <!-- 分析開始ボタン -->
    <div class="start-analysis">
      <button @click="startAnalysis" :disabled="!isFormValid">分析開始</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      file: null,  // 選択されたファイル
      youtubeUrl: "",  // 入力されたYouTubeURL
    };
  },
  computed: {
    // フォームが有効かどうかを判定
    isFormValid() {
      return this.file !== null || this.youtubeUrl !== "";
    }
  },
  methods: {
    // ファイル選択時にファイルを保存
    handleFileChange(event) {
      this.file = event.target.files[0];
    },
    // 分析開始ボタンが押された時の処理
    startAnalysis() {
      if (this.file) {
        console.log("ローカルファイルの分析開始:", this.file);
      }
      if (this.youtubeUrl) {
        console.log("YouTube URLの分析開始:", this.youtubeUrl);
      }
    }
  }
};
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.file-upload,
.youtube-url,
.start-analysis {
  margin-bottom: 20px;
}

.upload-label,
.youtube-label {
  margin-right: 10px;
}

input[type="file"] {
  margin-top: 10px;
}

input[type="url"] {
  margin-top: 10px;
  padding: 5px;
  width: 300px;
}

button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
}

button:hover {
  background-color: #45a049;
}
</style>
