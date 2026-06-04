import google.generativeai as genai
import time
import os
import sys

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Σφάλμα: Δεν βρέθηκε το GEMINI_API_KEY. Παρακαλώ όρισέ το.")
    sys.exit(1)

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.0-pro')

def main():
    print("==================================================")
    print("Έναρξη Πειράματος: Task Complexity")
    print("==================================================")
  
    print("Παρακαλώ περίμενε 10 δευτερόλεπτα...")
   
    time.sleep(10)
    
    print("\n Αποστολή ερωτήματος (prompt) στο Gemini...")
    
    prompt = "Γράψε έναν πλήρη, αντικειμενοστραφή κώδικα σε Python 300 γραμμών για ένα λειτουργικό παιχνίδι Tetris χρησιμοποιώντας τη βιβλιοθήκη pygame. Ο κώδικας πρέπει να περιλαμβάνει σύστημα βαθμολογίας, αυξανόμενα επίπεδα δυσκολίας, μενού αρχικής οθόνης και εξαιρετικά αναλυτικά σχόλια σε κάθε συνάρτηση. Στο τέλος, κάνε μια τεχνική ανάλυση της πολυπλοκότητας του αλγορίθμου ελέγχου συγκρούσεων (collision detection) που χρησιμοποίησες"
    
    start_time = time.time()
    
    try:
        response = model.generate_content(prompt)
        end_time = time.time()
        
        print("\n Λήφθηκε Απάντηση:")
        print("-" * 30)
        print(response.text.strip())
        print("-" * 30)
        
        print(f"\n Χρόνος απόκρισης API: {end_time - start_time:.2f} δευτερόλεπτα")
        
    except Exception as e:
        print(f"\n Υπήρξε σφάλμα κατά την κλήση του API: {e}")

    print("\n Το πείραμα ολοκληρώθηκε. Μπορείς να σταματήσεις.")

if __name__ == "__main__":
    main()
