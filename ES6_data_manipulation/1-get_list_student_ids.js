export default getListStudentIds;
const getListStudentIds = (theArray) => {
  if (!Array.isArray(theArray)) {
    return[];
  }
  return theArray.map((studentId) => studentId.id);
};

