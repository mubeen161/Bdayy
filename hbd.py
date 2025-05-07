import streamlit as st
from streamlit.components.v1 import html
import time
import base64
from datetime import datetime
import random

# Password configuration
PASSWORD = "1"

# Questions and answers
questions = [
    "Apan dono kaisa mille pehli baar?",
    "Woh kounsi jagah hai jab apan motto se pehli baar utti lambi baat karre thay?",
    "Last exam kab likhe apan?",
    "Apan kitte trips ku gaye na sab se zyada mast kounsi wali thi?",
    "Mere phone mei tera naam kya saved hai",
    "Woh kounsa time tha jab tu mei saath mei jaana start kare?"
]

answers = [
    ["late aaye jab", "Phy lab", "phy lab", "Graphics lab", "graphics lab","1"],
    ["masjid", "masjid k paas ki bench", "masjid ke paas ki benech","2"],
    ["24 june 2024", "24 june", "24/06/24", "24-06-2024","3"],
    ["ooty", "vizag", "odisha", "anantragirri hills", "SIH", "sih","4"],
    ["Mubbu buddy", "mubbu buddy", "Mubbu Buddy","5"],
    ["1st sem exams", "2nd sem exams", "exams", "1st year exams", "external exams", "1st year exams","6"]
]

hints = [
    "Wali millaya tha apne ku, tu chair pe tha. Koi lab tha dekh",
    "BRUHHH YEH YAAD NAI HAI",
    "SOCHO SOCHO",
    "ITTA KYA SOCHRA RE BHAI",
    "CHIIIIII Yeh nai mllm",
    "Kuch toh tha ek imp din tha... tu bola aaj bawa gaadi leke nai gaye mei pick karletu."
]

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        
        audio_html = f"""
        <div id="audio-container"></div>
        <script>
            const audio = document.createElement('audio');
            audio.src = "data:audio/mp3;base64,{b64}";
            audio.autoplay = true;
            audio.loop = true;
            document.getElementById('audio-container').appendChild(audio);
            
            function playAudio() {{
                audio.play().catch(e => console.log('Audio play failed:', e));
            }}
            
            function stopAudio() {{
                audio.pause();
                audio.currentTime = 0;
            }}
            
            // Play audio when user interacts with the page
            document.addEventListener('click', playAudio, {{ once: true }});
            
            // Store functions in global scope for later use
            window.playBirthdayAudio = playAudio;
            window.stopBirthdayAudio = stopAudio;
        </script>
        """
        html(audio_html)

def stop_audio():
    stop_audio_js = """
    <script>
        if (window.stopBirthdayAudio) {
            stopBirthdayAudio();
        }
    </script>
    """
    html(stop_audio_js)

# Confetti animation
def confetti_animation():
    confetti_js = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
    function fireConfetti() {
        // Left edge
        confetti({
            particleCount: 100,
            angle: 60,
            spread: 55,
            origin: { x: 0 }
        });
        
        // Right edge
        confetti({
            particleCount: 100,
            angle: 120,
            spread: 55,
            origin: { x: 1 }
        });
        
        // Center burst
        confetti({
            particleCount: 150,
            spread: 70,
            origin: { y: 0.6 }
        });
    }
    
    // Fire confetti when page loads
    window.addEventListener('load', fireConfetti);
    </script>
    """
    html(confetti_js)

# Balloon animation
def balloon_animation():
    balloon_js = """
    <script>
    function createBalloons() {
        const container = document.querySelector('.main');
        const colors = ['#ff0000', '#ff7f00', '#ffff00', '#00ff00', '#0000ff', '#4b0082', '#9400d3', '#ff1493', '#00ffff'];
        
        for (let i = 0; i < 50; i++) {
            const balloon = document.createElement('div');
            balloon.className = 'balloon';
            balloon.style.left = Math.random() * 100 + 'vw';
            balloon.style.width = (Math.random() * 40 + 20) + 'px';
            balloon.style.height = (Math.random() * 50 + 40) + 'px';
            balloon.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            balloon.style.animationDuration = (Math.random() * 8 + 5) + 's';
            balloon.style.animationDelay = (Math.random() * 3) + 's';
            
            // Add balloon string
            const string = document.createElement('div');
            string.className = 'balloon-string';
            string.style.width = '2px';
            string.style.height = (Math.random() * 50 + 30) + 'px';
            string.style.backgroundColor = '#cccccc';
            string.style.position = 'absolute';
            string.style.bottom = '-' + string.style.height;
            string.style.left = '50%';
            string.style.transform = 'translateX(-50%)';
            
            balloon.appendChild(string);
            container.appendChild(balloon);
        }
    }
    
    // Add CSS for balloons
    const style = document.createElement('style');
    style.textContent = `
        .balloon {
            position: fixed;
            bottom: -100px;
            border-radius: 50%;
            opacity: 0.8;
            animation-name: float-up;
            animation-timing-function: ease-in;
            animation-iteration-count: infinite;
            z-index: 999;
            box-shadow: inset -5px -5px 10px rgba(0,0,0,0.2);
        }
        
        .balloon-string {
            position: absolute;
            bottom: -30px;
            left: 50%;
            transform: translateX(-50%);
            background-color: #cccccc;
            width: 2px;
        }
        
        @keyframes float-up {
            to {
                transform: translateY(-120vh);
                opacity: 0;
            }
        }
        
        .birthday-text {
            font-size: 5rem !important;
            font-weight: bold !important;
            text-align: center !important;
            margin: 2rem 0 !important;
            background: linear-gradient(to right, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #4b0082, #9400d3);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: shine 1.5s infinite, rainbow 5s infinite;
            text-shadow: 0 0 15px rgba(255,255,255,0.7);
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        
        @keyframes shine {
            0% { filter: brightness(1); }
            50% { filter: brightness(1.5); }
            100% { filter: brightness(1); }
        }
        
        @keyframes rainbow {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }
        
        .heart {
            color: red;
            animation: heartbeat 1.5s infinite;
            display: inline-block;
        }
        
        @keyframes heartbeat {
            0% { transform: scale(1); }
            25% { transform: scale(1.1); }
            50% { transform: scale(1); }
            75% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        .emoji {
            font-size: 2rem;
            animation: float 3s ease-in-out infinite;
            display: inline-block;
        }
        
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
            100% { transform: translateY(0px); }
        }
    `;
    document.head.appendChild(style);
    
    // Create balloons when page loads
    window.addEventListener('load', createBalloons);
    </script>
    """
    html(balloon_js)

# Floating emojis
def floating_emojis():
    emojis = ["🎉", "🎈", "🎁", "🥳", "✨", "🎊", "❤️", "🌟", "💫"]
    emoji_html = "".join([f'<span class="emoji" style="animation-delay: {i*0.5}s;">{emoji}</span>' for i, emoji in enumerate(emojis*3)])
    st.markdown(f'<div style="text-align: center; margin: 20px 0;">{emoji_html}</div>', unsafe_allow_html=True)

# Main app
def main():
    st.set_page_config(page_title="Birthday Surprise", layout="wide", initial_sidebar_state="collapsed")
    
    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'show_surprise' not in st.session_state:
        st.session_state.show_surprise = False
    if 'show_message' not in st.session_state:
        st.session_state.show_message = False
    if 'show_video1' not in st.session_state:
        st.session_state.show_video1 = False
    if 'show_video2' not in st.session_state:
        st.session_state.show_video2 = False
    if 'lights_on' not in st.session_state:
        st.session_state.lights_on = False
    if 'audio_played' not in st.session_state:
        st.session_state.audio_played = False
    
    # Play audio immediately when app loads
    if not st.session_state.audio_played:
        autoplay_audio("Happy Birthday To You Ji-(Mr-Jat.in).mp3")
        st.session_state.audio_played = True
    
    # Password screen
    if not st.session_state.authenticated:
        st.markdown("""
        <style>
        .password-container {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 3rem;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            max-width: 600px;
            margin: 0 auto;
            text-align: center;
        }
        .password-title {
            font-size: 2.5rem;
            color: #4b0082;
            margin-bottom: 1.5rem;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .password-input {
            margin: 1.5rem 0;
        }
        .password-button {
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            color: white;
            border: none;
            padding: 0.8rem 2rem;
            font-size: 1.2rem;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .password-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="password-container">
            <div class="password-title">🎂 Mubbu's Birthday Surprise 🎂</div>
            <p style="font-size: 1.2rem; color: #555;">Enter the secret password to unlock the celebration!</p>
            <div class="password-input">
        """, unsafe_allow_html=True)
        
        password = st.text_input("Enter password:", type="password", label_visibility="collapsed")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("🚀 Unlock the Magic!", key="password_button"):
            if password == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password. Try again!")
                st.markdown('<div style="text-align: center; margin-top: 1rem;">🔒</div>', unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Add some floating emojis in the background
        st.markdown("""
        <style>
        .floating-emoji {
            position: fixed;
            font-size: 2rem;
            animation: float 5s ease-in-out infinite;
            opacity: 0.7;
        }
        @keyframes float {
            0% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-50px) rotate(10deg); }
            100% { transform: translateY(0px) rotate(0deg); }
        }
        </style>
        <div class="floating-emoji" style="left: 10%; top: 20%; animation-delay: 0s;">🎈</div>
        <div class="floating-emoji" style="left: 25%; top: 70%; animation-delay: 1s;">🎁</div>
        <div class="floating-emoji" style="left: 50%; top: 30%; animation-delay: 2s;">🎊</div>
        <div class="floating-emoji" style="left: 75%; top: 60%; animation-delay: 3s;">✨</div>
        <div class="floating-emoji" style="left: 90%; top: 20%; animation-delay: 4s;">🥳</div>
        """, unsafe_allow_html=True)
        
        return
    
    # Quiz questions
    if not st.session_state.show_surprise and st.session_state.current_question < len(questions):
        st.markdown("""
        <style>
        .quiz-container {
            background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        .quiz-title {
            font-size: 2rem;
            color: #4b0082;
            margin-bottom: 1rem;
            text-align: center;
            font-weight: bold;
        }
        .quiz-question {
            font-size: 1.5rem;
            color: #333;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        .quiz-hint {
            color: #ff6b6b;
            font-style: italic;
            margin-top: 0.5rem;
        }
        .quiz-button {
            background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            font-size: 1.1rem;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-top: 1rem;
        }
        .quiz-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        </style>
        """, unsafe_allow_html=True)
        
        current_q = st.session_state.current_question
        
        st.markdown(f"""
        <div class="quiz-container">
            <div class="quiz-title">🎉 Birthday Quiz 🎉</div>
            <div class="quiz-question">Question {current_q + 1}: {questions[current_q]}</div>
        </div>
        """, unsafe_allow_html=True)
        
        user_answer = st.text_input("Your answer:", key=f"answer_{current_q}", label_visibility="collapsed")
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button(f"Submit Answer {'✨' * (current_q + 1)}", key=f"submit_{current_q}"):
                if user_answer.lower() in [ans.lower() for ans in answers[current_q]]:
                    st.success(f"Correct! 🎉 {'🌟' * (current_q + 1)}")
                    confetti_animation()
                    time.sleep(1)
                    st.session_state.current_question += 1
                    if st.session_state.current_question >= len(questions):
                        st.session_state.show_surprise = True
                    st.rerun()
                else:
                    st.error(f"Oops! Try again ❌")
                    st.markdown(f'<div class="quiz-hint">Hint: {hints[current_q]}</div>', unsafe_allow_html=True)
        
        # Add progress
        st.markdown(f"""
        <div style="text-align: center; margin-top: 2rem;">
            <progress value="{current_q}" max="{len(questions)}" style="width: 80%; height: 10px;"></progress>
            <p>Progress: {current_q}/{len(questions)} questions answered</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Add some decorative elements
        floating_emojis()
        return
    
    # Show surprise section after all questions are answered
    if st.session_state.show_surprise and not st.session_state.show_message and not st.session_state.show_video1 and not st.session_state.show_video2:
        st.markdown("""
        <style>
        .surprise-container {
            text-align: center;
            margin: 3rem 0;
        }
        .surprise-button {
            background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
            background-size: 400% 400%;
            color: white;
            border: none;
            padding: 1.5rem 3rem;
            font-size: 2rem;
            border-radius: 50px;
            cursor: pointer;
            animation: gradient 8s ease infinite, pulse 2s infinite;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .surprise-button:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 30px rgba(0,0,0,0.3);
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="surprise-container"><button class="surprise-button" onclick="document.querySelector(\'button\').click()">✨ OPEN YOUR SURPRISE ✨</button></div>', unsafe_allow_html=True)
        
        if st.button("OPEN SURPRISE", key="open_surprise", help="Click to open your surprise"):
            st.session_state.lights_on = True
            balloon_animation()
            confetti_animation()
            st.markdown('<div class="birthday-text">HAPPY BIRTHDAY MUBBU!</div>', unsafe_allow_html=True)
            floating_emojis()
            st.session_state.show_message = True
            st.rerun()
    
    # Show message
    if st.session_state.show_message and not st.session_state.show_video1 and not st.session_state.show_video2:
        st.markdown("""
        <style>
        .message-container {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            margin: 2rem auto;
            max-width: 800px;
        }
        .message-title {
            font-size: 2rem;
            color: #4b0082;
            text-align: center;
            margin-bottom: 1.5rem;
            font-weight: bold;
        }
        .message-content {
            font-size: 1.2rem;
            line-height: 1.8;
            color: #333;
        }
        .next-button {
            background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
            color: white;
            border: none;
            padding: 1rem 2rem;
            font-size: 1.2rem;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin: 2rem auto;
            display: block;
        }
        .next-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="message-container">
            <div class="message-title">💌 A Special Message For You 💌</div>
            <div class="message-content">
                Mubashir - "Bringer Of Good News, Spreader Of Good News" 🤌🏻<br><br>
                Isn't it fun to think about how far we've come since we first met? Khair for sure never thought it willl be sooo enjoyable and roller coaster ride. Legit almost sab cheezo k liye tere paas aajatu mei bindas. And bgn bhi na sharam aati ya kuch hota. Mast chill hai sab. And teri family joh merku apna samjhti...ufff bht acha feel hota. Merku kuch bhi masla raho . The one person i turn to is YOU. Toppp se toppp secrets mllm re bhai terku. I can just blinding trust you. Nd in return i dont knoww mei kya karra tere liye. Khair India ku aaja mast enjoy karinge . Aur memories banainge. Aur time spent karinge. Aur kuppa kardinge. Missing you meri jaan....!!!<br><br>
            
                   Woich hai bhai friends like you are unique. Friends may come and go, but real ones never leave. 🤧
            Allah aapki aage ke kaamo mei aasani farmade . Allah aapke kaamo mei barkat dede. 
                    Aapku aapka kaam karne mei maza aana passion se karna.
                     Jaldi masters hojana. Sukoon se family k paas rehna. Ya Allah iski jaldi shadi hojana aur meri bhi. 
                    Waha ke loga kaise hai ki kya rehta ki magar terku mllm tere struggles. Ya Allah make it easy for you. 
                    i hope you have lots of fun.
                
                And i hope you stay connected and consistent with Allah even more so than you are right now
                
                Ameen Ya Rabbul Al-Ameen
            
        </div>
        """, unsafe_allow_html=True)
        
        floating_emojis()
        
        if st.button("🎬 SEE MORE MEMORIES 🎬", key="see_more", help="Click to see more"):
            st.session_state.show_message = False
            st.session_state.show_video1 = True
            st.rerun()
    
    # Show first video
    if st.session_state.show_video1 and not st.session_state.show_video2:
        # Stop the audio when videos start playing
        stop_audio()
        
        st.markdown("""
        <style>
        .video-container {
            background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            margin: 2rem auto;
            max-width: 800px;
            text-align: center;
        }
        .video-title {
            font-size: 2rem;
            color: #4b0082;
            margin-bottom: 1.5rem;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="video-container">
            
        </div>
        """, unsafe_allow_html=True)
        
        # Replace with your actual video file
        st.video("main.mp4")
        
        floating_emojis()
        
        if st.button("🎥 AUR BHI HAI! 🎥", key="more_content", help="Click to see more videos"):
            st.session_state.show_video1 = False
            st.session_state.show_video2 = True
            st.rerun()
    
    # Show second video
    if st.session_state.show_video2:
        st.markdown("""
        <style>
        .final-container {
            text-align: center;
            margin: 3rem 0;
        }
        .final-text {
            font-size: 2rem;
            color: #4b0082;
            margin-bottom: 2rem;
            font-weight: bold;
            animation: rainbow 5s infinite;
        }
        @keyframes rainbow {
            0% { color: #ff0000; }
            14% { color: #ff7f00; }
            28% { color: #ffff00; }
            42% { color: #00ff00; }
            57% { color: #0000ff; }
            71% { color: #4b0082; }
            85% { color: #9400d3; }
            100% { color: #ff0000; }
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="video-container">
            
        </div>
        """, unsafe_allow_html=True)
        
        # Replace with your actual video file
        st.video("Axel - Formal Sitting.mp4")
        
        st.markdown("""
        <div class="final-container">
            <div class="final-text">❤️ Thank You For Being You! ❤️</div>
            <div style="font-size: 1.5rem; margin-bottom: 2rem;">May this year be filled with joy, success, and wonderful memories!</div>
            <div class="heart" style="font-size: 3rem;">♥️</div>
        </div>
        """, unsafe_allow_html=True)
        
        confetti_animation()
        floating_emojis()

if __name__ == "__main__":
    main()