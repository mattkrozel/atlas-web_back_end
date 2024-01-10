/* eslint-disable */
export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const decider = true;
    if (decider) {
      resolve('true');
    } else {
      reject(new Error('false error message'));
    }
  });
}
