const getListStudentIds = (theArray) => {
  if (!Array.isArray(theArray)) {
    return [];
  }
  return theArray.map((studentId) => studentId.id);
};

export default getListStudentIds;
