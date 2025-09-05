// Simple test script to verify mobile app can connect to backend
// Run this in the mobile directory: node test-connection.js

const API_BASE_URL = 'https://busybeeapp.onrender.com/api';

async function testConnection() {
  console.log('🧪 Testing mobile app connection to backend...');
  
  try {
    // Test health endpoint
    console.log('\n1. Testing health endpoint...');
    const healthResponse = await fetch(`${API_BASE_URL}/health`);
    if (healthResponse.ok) {
      const healthData = await healthResponse.json();
      console.log('   ✅ Health check passed:', healthData.status);
    } else {
      console.log('   ❌ Health check failed:', healthResponse.status);
    }
    
    // Test tasks endpoint
    console.log('\n2. Testing tasks endpoint...');
    const tasksResponse = await fetch(`${API_BASE_URL}/tasks`);
    if (tasksResponse.ok) {
      const tasksData = await tasksResponse.json();
      console.log('   ✅ Tasks fetch successful:', tasksData.length, 'tasks found');
      console.log('   📋 Sample tasks:', tasksData.slice(0, 3).map(t => t.text));
    } else {
      console.log('   ❌ Tasks fetch failed:', tasksResponse.status);
    }
    
    // Test creating a task
    console.log('\n3. Testing task creation...');
    const createResponse = await fetch(`${API_BASE_URL}/tasks`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: 'Test task from mobile connection test' }),
    });
    
    if (createResponse.ok) {
      const createData = await createResponse.json();
      console.log('   ✅ Task creation successful:', createData.text);
      
      // Test updating the task
      console.log('\n4. Testing task update...');
      const updateResponse = await fetch(`${API_BASE_URL}/tasks/${createData.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ done: true }),
      });
      
      if (updateResponse.ok) {
        console.log('   ✅ Task update successful');
      } else {
        console.log('   ❌ Task update failed:', updateResponse.status);
      }
    } else {
      console.log('   ❌ Task creation failed:', createResponse.status);
    }
    
    console.log('\n🎉 Connection test completed successfully!');
    console.log('📱 The mobile app should be able to connect to the backend.');
    
  } catch (error) {
    console.log('\n❌ Connection test failed:', error.message);
    console.log('🔧 Make sure the Flask backend is running on', API_BASE_URL);
  }
}

// Run the test
testConnection();
