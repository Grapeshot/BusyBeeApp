import React, { useState } from 'react';
import { 
  View, 
  Text, 
  TextInput, 
  TouchableOpacity, 
  Alert, 
  StyleSheet, 
  ActivityIndicator
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const API_BASE_URL = 'https://busybeeapp.onrender.com/api';

export default function RegisterScreen({ onRegisterSuccess, onBackToLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleRegister = async () => {
    if (!username || !password) {
      Alert.alert('Error', 'Please enter both username and password');
      return;
    }

    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (response.ok) {
        Alert.alert('Success', 'User registered successfully!');
        onRegisterSuccess(username, password); // Optionally auto-login
      } else {
        Alert.alert('Error', data.error || 'Registration failed');
      }
    } catch (err) {
      Alert.alert('Error', 'Network error: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Ionicons name="bee" size={64} color="#FFD700" />
      <Text style={styles.title}>BusyBee Register</Text>

      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />

      <TouchableOpacity 
        style={[styles.button, loading && styles.buttonDisabled]} 
        onPress={handleRegister} 
        disabled={loading}
      >
        {loading ? <ActivityIndicator color="#fff" /> : <Text style={styles.buttonText}>Register</Text>}
      </TouchableOpacity>

      <TouchableOpacity onPress={onBackToLogin} style={{ marginTop: 16 }}>
        <Text style={{ color: '#333', textDecorationLine: 'underline' }}>Back to Login</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { 
    flex:1, 
    justifyContent:'center', 
    alignItems:'center', 
    padding:20, 
    backgroundColor:'#f8f9fa' },
  title: {
    fontSize:28,
    fontWeight:'bold',
    marginVertical:20,
    color:'#333' },
  input: {
    width:'100%', 
    borderWidth:1, 
    borderColor:'#ddd', 
    borderRadius:8, 
    paddingHorizontal:16, 
    paddingVertical:12, 
    fontSize:16, 
    backgroundColor:'#fff', 
    marginBottom:12 },
  button: { 
    backgroundColor:'#4CAF50', 
    borderRadius:8, 
    paddingVertical:12, 
    paddingHorizontal:32, 
    alignItems:'center' },
  buttonDisabled: { backgroundColor:'#ccc' },
  buttonText: { color:'#fff', fontSize:18, fontWeight:'600' },
});
