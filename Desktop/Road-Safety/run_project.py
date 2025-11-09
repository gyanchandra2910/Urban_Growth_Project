"""
Road Safety Recommendation System - One-Click Launcher
Starts Flask API and Streamlit UI with health checks and real-time logs
"""

import subprocess
import time
import webbrowser
import sys
import threading
import requests
from queue import Queue, Empty

def read_output(pipe, queue, label):
    """Read process output and forward to console in real-time"""
    try:
        for line in iter(pipe.readline, ''):
            if line:
                sys.stdout.write(f"[{label}] {line}")
                sys.stdout.flush()
                queue.put(line)
    except:
        pass
    finally:
        pipe.close()

def check_health(url, timeout=30):
    """Poll URL until it returns 200 or timeout"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                return True
        except requests.exceptions.RequestException:
            pass
        time.sleep(1)
    return False

def main():
    print("\n" + "="*80)
    print("🚦 ROAD SAFETY RECOMMENDATION SYSTEM - LAUNCHER")
    print("="*80 + "\n")
    
    flask_process = None
    streamlit_process = None
    flask_output = Queue()
    streamlit_output = Queue()
    
    try:
        # Use Python 3.13 explicitly (where packages are installed)
        python_exe = r"C:\Users\91995\AppData\Local\Programs\Python\Python313\python.exe"
        
        # Start Flask server
        print("🚀 Starting Flask server...")
        flask_process = subprocess.Popen(
            [python_exe, "app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Start thread to read Flask output
        flask_thread = threading.Thread(
            target=read_output,
            args=(flask_process.stdout, flask_output, "FLASK"),
            daemon=True
        )
        flask_thread.start()
        
        time.sleep(1)
        
        # Start Streamlit server
        print("🌐 Starting Streamlit server...")
        streamlit_process = subprocess.Popen(
            [python_exe, "-m", "streamlit", "run", "streamlit_app.py", "--server.headless=true"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Start thread to read Streamlit output
        streamlit_thread = threading.Thread(
            target=read_output,
            args=(streamlit_process.stdout, streamlit_output, "STREAMLIT"),
            daemon=True
        )
        streamlit_thread.start()
        
        # Wait for both servers to become healthy
        print("\n⏳ Waiting for servers to become healthy (up to 30 seconds)...")
        
        # Check Flask health
        print("   Checking Flask at http://127.0.0.1:5000/health ...")
        flask_healthy = check_health("http://127.0.0.1:5000/health", timeout=30)
        
        if not flask_healthy:
            print("\n❌ ERROR: Flask server did not become healthy within 30 seconds")
            print("\nLast Flask output:")
            recent_output = []
            try:
                while True:
                    recent_output.append(flask_output.get_nowait())
            except Empty:
                pass
            print("".join(recent_output[-200:] if len("".join(recent_output)) > 200 else recent_output))
            return 1
        
        print("   ✓ Flask server is healthy")
        
        # Check Streamlit health
        print("   Checking Streamlit at http://localhost:8501 ...")
        streamlit_healthy = check_health("http://localhost:8501", timeout=30)
        
        if not streamlit_healthy:
            print("\n❌ ERROR: Streamlit server did not become healthy within 30 seconds")
            print("\nLast Streamlit output:")
            recent_output = []
            try:
                while True:
                    recent_output.append(streamlit_output.get_nowait())
            except Empty:
                pass
            print("".join(recent_output[-200:] if len("".join(recent_output)) > 200 else recent_output))
            return 1
        
        print("   ✓ Streamlit server is healthy")
        
        # Open browser
        print("\n🌍 Opening browser at http://localhost:8501 ...")
        webbrowser.open("http://localhost:8501")
        
        print("\n" + "="*80)
        print("✅ BOTH SERVERS ARE RUNNING")
        print("="*80)
        print("\n📊 Access Points:")
        print("   • Flask API:    http://127.0.0.1:5000")
        print("   • Streamlit UI: http://localhost:8501")
        print("\n💡 Press CTRL+C to stop both servers")
        print("="*80 + "\n")
        
        # Keep the script running and monitor processes
        while True:
            time.sleep(1)
            
            # Check if processes are still running
            if flask_process.poll() is not None:
                print("\n⚠️  Flask server stopped unexpectedly (exit code: {})".format(flask_process.poll()))
                break
            if streamlit_process.poll() is not None:
                print("\n⚠️  Streamlit server stopped unexpectedly (exit code: {})".format(streamlit_process.poll()))
                break
    
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down servers...")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return 1
    
    finally:
        # Terminate processes
        if flask_process and flask_process.poll() is None:
            flask_process.terminate()
            try:
                flask_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                flask_process.kill()
            print("✓ Flask server stopped")
        
        if streamlit_process and streamlit_process.poll() is None:
            streamlit_process.terminate()
            try:
                streamlit_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                streamlit_process.kill()
            print("✓ Streamlit server stopped")
        
        print("\n👋 Goodbye!\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
