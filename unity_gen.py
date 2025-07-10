def generate_unity_script(name):
    return f"""
using UnityEngine;

public class {name} : MonoBehaviour {{
    void Start() {{
        Debug.Log("Level {name} loaded!");
    }}
}}
"""
