function add_field(par, par2) {
    par += 1
    console.log(par)
    window.location.href=`http://localhost:8000/${par}/${par2}`
}
function delete_field(par, par2) {
    if (par === 1) return
    par -= 1
    console.log(par)
    window.location.href=`http://localhost:8000/${par}/${par2}`
}
function add_file_field(par, par2) {
    par2 += 1
    console.log(par2)
    window.location.href=`http://localhost:8000/${par}/${par2}`
}
function delete_file_field(par, par2) {
    if (par2 === 1) return
    par2 -= 1
    console.log(par2)
    window.location.href=`http://localhost:8000/${par}/${par2}`
}