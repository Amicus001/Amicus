nums = []
print(f'nums = {len(nums)}개, {nums}')
nums.append(99)

#리스트에 데이터를 추가하는 메서드 = insert(index, data)
nums.insert(0, 2024)
print(f'nums = {len(nums)}개, {nums}')

nums.insert(-1,["asdf", "zxcv"])
print(f'nums = {len(nums)}개, {nums}')

#"zxcv" 데이터 삭제
del(nums[-1])

#모든 원소를 삭제하여 빈 리스트로 만들기
del(nums[:])
print(nums)

# 리스트 안의 원소(요소) 정렬; 오름차순 기본

nums.append(9)
nums.append(15)
nums.append(-33)
nums.append(345)
nums.append(0.59)

nums.sort()

print(f'nums = {len(nums)}개, {nums}')

#내림차순 정렬
nums.sort(reverse=True)


#원소의 현재 위치를 거꾸로(값 비교 없이) 순서만 바꾸기.
nums.reverse()

#리스트 안에서 지정된 원소(요소)를 삭제하는 메서드; remove
nums.remove(9)

# 리스트의 원소/요소를 꺼내는 메서드; pop()
nums.append(55)
nums.append(64)
nums.append(99)

nums.pop()
print(nums)
nums.append([100,200])
#list에서 특정 원소(요소) 데이터가 몇 개 존재하는지 세어주는 메서드; count(data)
#extend(); 리스트 확장

#nums.extend([11,22,33]) 시퀀스/반복 가능한 데이터만 가능.
#리스트를 얕은 복사하는 메서드; copy()
nums2 = nums.copy()
#nums의 -1번 요소의 데이터를 2024로 변경
nums[1] = 2024

#nums의 -1번 요소의 0번 요소의 데이터를 77로 변경
nums[1][0]=77

print(f'nums = {len(nums)}개, {nums}')
print(f'nums2 = {len(nums2)}개, {nums2}')
