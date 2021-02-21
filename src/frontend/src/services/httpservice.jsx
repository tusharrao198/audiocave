// import axios from 'axios';
// import {toast} from 'react-toastify';
 

// axios.interceptors.use(null, error => {
//     const expectedError = error.response && error.response.status>=400 && error.response.status < 500;
    
//     if (!expectedError) {
//         console.log("Logging the error",error);
//         toast.error("An Unexpected Error Occured");
//         // toast("An Unexpected Error Occured"); // alternate for alert
//     }

//     return Promise.reject(error);
// });

// export default {
//     get: axios.get,
//     put: axios.put,
//     delete: axios.delete,
//     post: axios.post,
// };