from collections import deque

def find_word_ladder(start_word, end_word, word_list):
    """
    Başlangıç kelimesinden bitiş kelimesine en kısa kelime merdivenini bulur.
    BFS algoritmasını kullanır.

    Args:
        start_word (str): Merdivenin başlangıç kelimesi.
        end_word (str): Merdivenin hedef kelimesi.
        word_list (list): Geçerli kelimeleri içeren sözlük.

    Returns:
        list: En kısa kelime merdiveni yolunu içeren kelime listesi.
              Eğer yol bulunamazsa boş liste döner.
    """
    # Başlangıç ve bitiş kelimeleri sözlükte olmalı ve aynı uzunlukta olmalı
    if end_word not in word_list or start_word not in word_list or \
       len(start_word) != len(end_word):
        return []

    # BFS için kuyruk: (mevcut_kelime, mevcut_yol)
    queue = deque([(start_word, [start_word])])
    # Ziyaret edilen kelimeleri takip etmek için küme
    visited = {start_word}
    # Hızlı kelime araması için sözlüğü kümeye çevir
    word_set = set(word_list)

    while queue:
        current_word, path = queue.popleft()

        # Hedefe ulaşıldıysa yolu döndür
        if current_word == end_word:
            return path

        # Mevcut kelimenin her harfini değiştirerek komşuları bul
        for i in range(len(current_word)):
            original_char = current_word[i]
            # Alfabedeki her harfi dene (Türkçe karakterler dahil)
            # Not: Bu basit örnekte tüm Türkçe karakter dönüşümleri tam olarak ele alınmamıştır.
            # Gerçek bir uygulamada daha kapsamlı bir alfabe ve dönüşüm mantığı gerekebilir.
            for char_code in range(ord('a'), ord('z') + 1):
                char = chr(char_code)
                # Türkçe özel karakterler için basit dönüşümler
                if char == 'i' and original_char == 'i': char = 'ı' # 'i' yerine 'ı' denenebilir
                elif char == 'i' and original_char == 'İ': char = 'i' # 'İ' yerine 'i' denenebilir
                
                temp_word_list = list(current_word)
                temp_word_list[i] = char
                next_word = "".join(temp_word_list)

                # Oluşturulan kelime sözlükte varsa ve daha önce ziyaret edilmediyse
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, path + [next_word]))
            
            # Türkçe özel karakterler için ek kontrol (ç, ğ, ı, ö, ş, ü)
            turkish_chars = ['ç', 'ğ', 'ı', 'ö', 'ş', 'ü']
            for t_char in turkish_chars:
                if original_char != t_char: # Kendi harfiyle değiştirmemek için
                    temp_word_list = list(current_word)
                    temp_word_list[i] = t_char
                    next_word = "".join(temp_word_list)
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, path + [next_word]))


    return [] # Yol bulunamazsa boş liste döndür

# Örnek Kullanım ve Farklı Sözlükler:

# Sözlük 1: Temel Örnek
sample_dictionary_1 = ["kedi", "koki", "koçi", "kuçi", "kuçu", "keçi", "kuzu", "kasa", "kara", "masa", "maşa", "şaka", "saka", "sana", "mana"]
start_1 = "kedi"
end_1 = "kuçu"

ladder_1 = find_word_ladder(start_1, end_1, sample_dictionary_1)
print(f"Sözlük 1 - '{start_1}' -> '{end_1}': {' -> '.join(ladder_1) if ladder_1 else 'Yol bulunamadı.'}")

start_1_b = "masa"
end_1_b = "şaka"
ladder_1_b = find_word_ladder(start_1_b, end_1_b, sample_dictionary_1)
print(f"Sözlük 1 - '{start_1_b}' -> '{end_1_b}': {' -> '.join(ladder_1_b) if ladder_1_b else 'Yol bulunamadı.'}")


# Sözlük 2: Daha Uzun Kelimeler ve Farklı Bağlantılar
sample_dictionary_2 = ["elma", "alma", "arma", "arpa", "arka", "parka", "parça", "pazı", "sazı", "kazı", "kuzu", "kuru", "boru", "doru", "dolu"]
start_2 = "elma"
end_2 = "arka"

ladder_2 = find_word_ladder(start_2, end_2, sample_dictionary_2)
print(f"Sözlük 2 - '{start_2}' -> '{end_2}': {' -> '.join(ladder_2) if ladder_2 else 'Yol bulunamadı.'}")

start_2_b = "kuzu"
end_2_b = "dolu"
ladder_2_b = find_word_ladder(start_2_b, end_2_b, sample_dictionary_2)
print(f"Sözlük 2 - '{start_2_b}' -> '{end_2_b}': {' -> '.join(ladder_2_b) if ladder_2_b else 'Yol bulunamadı.'}")


# Sözlük 3: Yolun Bulunamadığı Durum
sample_dictionary_3 = ["ev", "at", "top", "gül", "buz"]
start_3 = "ev"
end_3 = "gül"

ladder_3 = find_word_ladder(start_3, end_3, sample_dictionary_3)
print(f"Sözlük 3 - '{start_3}' -> '{end_3}': {' -> '.join(ladder_3) if ladder_3 else 'Yol bulunamadı.'}")

# Sözlük 4: Başlangıç ve Bitiş Kelimelerinin Aynı Olduğu Durum
sample_dictionary_4 = ["test", "tost", "post"]
start_4 = "test"
end_4 = "test"

ladder_4 = find_word_ladder(start_4, end_4, sample_dictionary_4)
print(f"Sözlük 4 - '{start_4}' -> '{end_4}': {' -> '.join(ladder_4) if ladder_4 else 'Yol bulunamadı.'}")

