import java.util.*;

// set of stickers that spell a word
// /*google" "legolego" "leg" count_stickers(sticker_word, word)
//
// sticker word "google"
// desired word "legolego"*/
public class Stickers {
   public int countStickers(String stickerWord, String word) {
        HashMap<Character, Integer> wordCount = new HashMap<>();

        for (int i = 0; i < stickerWord.length(); i++) {
            int count = wordCount.containsKey(stickerWord.charAt(i)) ? wordCount.get(stickerWord.charAt(i)) : 0;
            wordCount.put(stickerWord.charAt(i), count + 1);
        }
        for (int i = 0; i < word.length(); i++) {
            int count = wordCount.containsKey(stickerWord.charAt(i)) ? wordCount.get(stickerWord.charAt(i)) : 0;
            if (word.charAt(i) == wordCount.get(word.charAt(i))) {
                wordCount.put(word.charAt(i), count - 1);
            }
        }
        return 5;
   } 
}
