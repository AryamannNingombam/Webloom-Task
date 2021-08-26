import {
    createAsyncThunk,
    createSlice
} from '@reduxjs/toolkit';
import {
    CheckVerified,
    SignIn
} from '../../services/auth.service';

const initialState = {
    token: null,
    signedIn: false,
    verified:false,
};


export const SignInUser = createAsyncThunk(
    'auth/SignInUser',
    async (body) => {
        const response = await SignIn(body);
        console.log("RESPONSE");
        console.log(response.data);
        const check = await CheckVerified(body.username,response.data.access);
        console.log("CHECK");
        console.log(check.data);
        return {
            tokenData : response.data,
            check : check.data  
        };
    }
);

export const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        changeToken: (state, action) => {
            state.token = action.payload.token;
        },
        logout : (state,action)=>{
            state.token =null;
        }

    },
    extraReducers: (builder) => {
        builder
            .addCase(SignInUser.fulfilled, (state, action) => {
                console.log(action.payload);
                state.token = action.payload.tokenData.access;
                state.verified = action.payload.check.verified;

            })
            .addCase(SignInUser.rejected, (state, action) => {
                console.log("REJECTED");
                state.token = null;
                state.signedIn = false;
            })


    },
});

export const {
    changeToken,
    logout
} = authSlice.actions;


export default authSlice.reducer;