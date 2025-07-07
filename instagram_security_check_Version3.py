import re
import os

def show_banner():
    banner = r"""
    #############################################
    #                                           #
    #      Instagram Security Check Tool        #
    #          ابزار تست امنیت اینستاگرام        #
    #                                           #
    #############################################
    #  استفاده فقط برای یادگیری و حساب شخصی     #
    #  هرگونه سوء استفاده غیرقانونی است  
    # سازنده این ابزار تیم ناسا می باشد
    #############################################
    """
    os.system('clear' if os.name == 'posix' else 'cls')
    print(banner)

def password_strength(password):
    if len(password) < 8:
        return "ضعیف (کمتر از ۸ کاراکتر)"
    if not re.search(r"[A-Z]", password):
        return "متوسط (حرف بزرگ ندارد)"
    if not re.search(r"[a-z]", password):
        return "متوسط (حرف کوچک ندارد)"
    if not re.search(r"[0-9]", password):
        return "متوسط (عدد ندارد)"
    if not re.search(r"[^A-Za-z0-9]", password):
        return "متوسط (کاراکتر خاص ندارد)"
    return "قوی"

def main():
    show_banner()
    print("ابزار آموزشی تست امنیت حساب اینستاگرام")
    password = input("رمز عبور خود را وارد کنید: ")
    print(f"قدرت رمز عبور شما: {password_strength(password)}")
    print("\nآیا تایید دومرحله‌ای فعال است؟")
    print("به تنظیمات اینستاگرام بروید > Security > Two-Factor Authentication و مطمئن شوید فعال است.")
    print("\nنکات امنیتی بیشتر:")
    print("- رمز عبور را هرگز با کسی به اشتراک نگذارید.")
    print("- ایمیل‌های مشکوک را باز نکنید و اطلاعات وارد نکنید.")
    print("- از رمزهای تکراری در سایت‌های مختلف استفاده نکنید.")
    print("- اگر لاگین مشکوک مشاهده کردید، سریعاً رمز را تغییر دهید.")

if __name__ == "__main__":
    main()