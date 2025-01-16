const collapseElementList = document.querySelectorAll('.collapse')
const collapseList = [...collapseElementList].map(collapseEl => new bootstrap.Collapse(collapseEl))

const bsCollapse = new bootstrap.Collapse('#myCollapse', {
    toggle: false
  })