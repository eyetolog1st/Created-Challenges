import signal


correct_answers = {
    "Q1": "bank_durian_mangga_dua",
    "Q2": "rama_pratama_satria",
    "Q3": "projecta.py",
    "Q4": "adi_wirawan_putra",
    "Q5": "88432"
}


user_answers = {
    "Q1": "",
    "Q2": "",
    "Q3": "",
    "Q4": "",
    "Q5": ""
}


class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutException


def check_all_correct():
    for question in correct_answers:
        if user_answers[question].lower() != correct_answers[question].lower():
            return False
    return True


def input_with_timeout(prompt, timeout=10):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    try:
        answer = input(prompt)
        signal.alarm(0)  
        return answer
    except TimeoutException:
        print("\nTime's up!")
        exit()


while not check_all_correct():
    
    if user_answers["Q1"] == "":
        q1_answer = input_with_timeout("Q1: What bank was the suspect trying to rob? (bank_nama_bank): ").strip()
        if q1_answer.lower() == correct_answers["Q1"].lower():
            print("Correct!")
            user_answers["Q1"] = q1_answer
        else:
            print("Incorrect. Try again.")
            exit()

    if user_answers["Q2"] == "":
        q2_answer = input_with_timeout("Q2: The full name of the partner he was working with? (the_name_here): ").strip()
        if q2_answer.lower() == correct_answers["Q2"].lower():
            print("Correct!")
            user_answers["Q2"] = q2_answer
        else:
            print("Incorrect. Try again.")
            exit()

    if user_answers["Q3"] == "":
        q3_answer = input_with_timeout("Q3: What suspicious file was used to encrypt the files? (file.extension): ").strip()
        if q3_answer.lower() == correct_answers["Q3"].lower():
            print("Correct!")
            user_answers["Q3"] = q3_answer
        else:
            print("Incorrect. Try again.")
            exit()

    if user_answers["Q4"] == "":
        q4_answer = input_with_timeout("Q4: Full name of the main suspect that owns the computer we are investigating? (the_name_here): ").strip()
        if q4_answer.lower() == correct_answers["Q4"].lower():
            print("Correct!")
            user_answers["Q4"] = q4_answer
        else:
            print("Incorrect. Try again.")
            exit()

    if user_answers["Q5"] == "":
        q5_answer = input_with_timeout("Q5: The secret code (00000): ").strip()
        if q5_answer.lower() == correct_answers["Q5"].lower():
            print("Correct!")
            user_answers["Q5"] = q5_answer
        else:
            print("Incorrect. Try again.")
            exit()

print("nice analyzing heres the flag!!!: BeeCTF{n1ce_inv3stigative_sk1lls_sh3rl0ck}")
